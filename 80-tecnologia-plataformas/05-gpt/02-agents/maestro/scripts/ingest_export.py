#!/usr/bin/env python3
"""Ingestao governada de um export Claude.ai na arquitetura ECOSSISTEMA 15-08.

Deterministico e reexecutavel: o mesmo export produz sempre os mesmos
documento_id, rotas e conteudos. Executa o roteamento documental do Maestro
(context-first, um unico canonical_home por fato) e emite manifesto,
roteamento, mapa doc->arquivo e proveniencia.

Uso:
    python3 ingest_export.py --export <dir-do-export> --root <repo> [--dry-run]
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from orchestrator.registry import load_folder_registry  # noqa: E402

LOTE = 'export-claude-20260913'
PREFIXO_ID = 'DOC-CLX'
LIMITE_INGESTAO_BYTES = 100_000

# Roteamento documental: (regex sobre o nome do arquivo, destino registrado,
# classificacao, motivo). Ordem = precedencia. O motivo declara objeto+intencao
# +audiencia, nunca "bateu keyword" (config/ROUTING.md).
REGRAS = [
    (r'schema|ontolog|data.?dict|validated-bundle|evidence-map',
     '60-dados/70-schemas', 'CONFIRMADO',
     'Artefato de estrutura de dados: define campos e contratos consumidos por outros dominios.'),
    (r'master.?index|roteamento|indice|índice',
     '01-master-index/04-reports', 'CONFIRMADO',
     'Indice/mapa de referencia: pertence ao controle central, nao ao dominio de conteudo.'),
    (r'runbook|runb|processo|process-doc|\bsop\b|rotina|producao',
     '70-operacao-governanca/10-sops', 'CONFIRMADO',
     'Procedimento operacional repetivel: audiencia executora, saida = SOP versionado.'),
    (r'decision|decisao|decisão|\badr',
     '70-operacao-governanca/06-decisoes', 'DECISÃO',
     'Registro de decisao com alternativas e justificativa: autoridade sobre execucao futura.'),
    (r'plan|plano|mapa.?os|working.?backwards|task.?center|agora|depois|cronograma',
     '70-operacao-governanca/01-planos-acao', 'CONFIRMADO',
     'Plano/sequenciamento de execucao: governa o que entra em ciclo, nao e evidencia.'),
    (r'status.?report|audit|relatorio|relatório|dashboard|pem-area|evidenc',
     '70-operacao-governanca/09-evidence', 'REFERÊNCIA',
     'Relato de estado com evidencia: valor probatorio, congelado no tempo da emissao.'),
    (r'prd|frd|spec|scanner|produto|multicanal',
     '20-produtos/10-executar-app', 'CONFIRMADO',
     'Especificacao de produto: audiencia de engenharia/produto, vincula requisito a release.'),
    (r'copy|carrossel|carousel|editorial|social|midia|mídia|pack',
     '30-editorial-marketing/03-social', 'CONFIRMADO',
     'Ativo editorial/canal: audiencia publica, ciclo de campanha.'),
    (r'gtm|launch|investment|memorandum|business|bcg|brfing|briefing|inteligen|inteligên|ecossitema|ecossistema|sas-0',
     '10-business/01-planos', 'REFERÊNCIA',
     'Material estrategico de negocio: sustenta decisao empresarial e narrativa de investimento.'),
    (r'comercial|proposta|oferta|showroom',
     '40-comercial-servicos', 'CONFIRMADO',
     'Material comercial: audiencia cliente/prospect, ciclo de venda.'),
    (r'template|placeholder|prisma|workbook|mapa_tml|form|html',
     '90-assets-compartilhados/03-templates', 'REFERÊNCIA',
     'Peca reutilizavel entre dominios: vive em assets e e referenciada por link.'),
    (r'prompt|agent|maestro|slash|command|\bai\b|obsidian|terminal',
     '80-tecnologia-plataformas/05-gpt/01-prompts', 'CONFIRMADO',
     'Insumo de orquestracao de IA: consumido por agente, nao por leitor humano final.'),
]

ROTA_PENDENTE = ('00-dropzone/08-to-classify', 'PENDENTE',
                 'Contexto insuficiente para eleger um canonical_home; permanece na dropzone ate triagem humana.')

EXT_COM_FRONTMATTER = {'.md', '.txt'}
EXT_TEXTO = {'.md', '.txt', '.html', '.json', '.csv', '.yaml', '.yml'}


def sha256(texto):
    return hashlib.sha256(texto.encode('utf-8')).hexdigest()


def slug(nome):
    """Nome de arquivo estavel e portavel, preservando legibilidade."""
    nome = nome.replace('/', '__').strip()
    nome = re.sub(r'[^\w\s.\-—·+]', '', nome, flags=re.UNICODE)
    nome = re.sub(r'\s+', '-', nome).strip('-.')
    return nome or 'sem-nome'


def normaliza_nome(filename):
    base = slug(filename)
    ext = os.path.splitext(base)[1].lower()
    if ext not in EXT_TEXTO:
        base, ext = base + '.md', '.md'
    return base, ext


def rota(filename, conteudo):
    """Filename primeiro (sinal de intencao do autor); conteudo so como desempate.

    Nunca decide por keyword isolada sem um destino registrado: sem sinal em
    nenhuma das duas passagens, o material fica na dropzone como PENDENTE.
    """
    for alvo in (filename.lower(), conteudo[:4000].lower()):
        for padrao, destino, classificacao, motivo in REGRAS:
            if re.search(padrao, alvo, flags=re.IGNORECASE):
                return destino, classificacao, motivo
    return ROTA_PENDENTE


def carrega_export(export_dir):
    projetos, conversas, chats = [], [], []
    for p in sorted((export_dir / 'projects-000' / 'projects').glob('*.json')):
        projetos.append(json.loads(p.read_text(encoding='utf-8')))
    conv = export_dir / 'conversations-000' / 'conversations.json'
    if conv.exists():
        conversas = json.loads(conv.read_text(encoding='utf-8'))
    for p in sorted((export_dir / 'design_chats-000' / 'design_chats').glob('*.json')):
        chats.append(json.loads(p.read_text(encoding='utf-8')))
    return projetos, conversas, chats


def frontmatter(doc):
    return (
        '---\n'
        f"id: {doc['documento_id']}\n"
        f"folder_id: {doc['folder_id']}\n"
        f"tipo: documento-importado\n"
        f"status: {doc['classificacao'].lower()}\n"
        f"origem: {LOTE}\n"
        f"origem_filename: \"{doc['filename']}\"\n"
        f"sha256: {doc['sha256']}\n"
        f"projeto: ECOSSISTEMA_15-08_FILESYSTEM\n"
        '---\n\n'
    )


def ponteiro(doc, export_dir):
    return (
        f'{frontmatter(doc)}'
        f"# Ponteiro · {doc['filename']}\n\n"
        f"Conteudo com {doc['bytes']} bytes acima do limite de {LIMITE_INGESTAO_BYTES} "
        'bytes para versionamento. O original permanece no export de origem.\n\n'
        f"- `documento_id`: {doc['documento_id']}\n"
        f"- `sha256`: {doc['sha256']}\n"
        f"- `canonical_home` proposto: `{doc['canonical_home_proposto']}`\n"
        f"- Origem: `{export_dir.name}/projects-000/projects/{doc['projeto_uuid']}.json`\n"
        f"- Motivo da rota: {doc['motivo_rota']}\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--export', required=True, type=Path)
    ap.add_argument('--root', required=True, type=Path)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    export_dir, root = args.export.resolve(), args.root.resolve()
    registrados = {r['path'] for r in load_folder_registry()}
    folder_id_por_path = {r['path']: r['folder_id'] for r in load_folder_registry()}

    projetos, conversas, chats = carrega_export(export_dir)
    docs, vistos_sha, vistos_destino = [], {}, set()
    contador = 0

    for proj in sorted(projetos, key=lambda p: p['uuid']):
        if proj.get('is_starter_project'):
            continue
        for d in proj.get('docs', []):
            contador += 1
            conteudo = d.get('content') or ''
            h = sha256(conteudo)
            destino, classificacao, motivo = rota(d['filename'], conteudo)
            if destino not in registrados:
                destino, classificacao, motivo = ROTA_PENDENTE
            nome, ext = normaliza_nome(d['filename'])
            doc = {
                'documento_id': f'{PREFIXO_ID}-{contador:03d}',
                'filename': d['filename'],
                'sha256': h,
                'bytes': len(conteudo.encode('utf-8')),
                'ext': ext,
                'created_at': d.get('created_at'),
                'projeto_uuid': proj['uuid'],
                'projeto_nome': proj['name'],
                'classificacao': classificacao,
                'motivo_rota': motivo,
                'canonical_home_proposto': f'{destino}/{nome}',
            }

            if h in vistos_sha:
                # Um fato = um canonical_home. Duplicata exata vira relacao, nao copia.
                doc.update(acao='duplicata', canonical_home=vistos_sha[h]['canonical_home'],
                           folder_id=vistos_sha[h]['folder_id'],
                           duplicata_de=vistos_sha[h]['documento_id'])
                docs.append(doc)
                continue

            if doc['bytes'] >= LIMITE_INGESTAO_BYTES:
                destino_final = '00-dropzone/08-to-classify'
                nome_final = os.path.splitext(nome)[0] + '.ponteiro.md'
                doc['acao'] = 'ponteiro'
            else:
                destino_final, nome_final = destino, nome
                doc['acao'] = 'ingerido'

            caminho = f'{destino_final}/{nome_final}'
            n = 2
            while caminho in vistos_destino:  # mesmo nome, conteudo distinto
                stem, e = os.path.splitext(nome_final)
                caminho = f'{destino_final}/{stem}__v{n:02d}{e}'
                n += 1
            vistos_destino.add(caminho)
            doc['canonical_home'] = caminho
            doc['folder_id'] = folder_id_por_path[destino_final]
            doc['duplicata_de'] = ''
            vistos_sha[h] = doc
            docs.append(doc)

            if args.dry_run:
                continue
            destino_path = root / caminho
            destino_path.parent.mkdir(parents=True, exist_ok=True)
            if doc['acao'] == 'ponteiro':
                destino_path.write_text(ponteiro(doc, export_dir), encoding='utf-8')
            elif ext in EXT_COM_FRONTMATTER:
                destino_path.write_text(frontmatter(doc) + conteudo, encoding='utf-8')
            else:
                # HTML/JSON/CSV/YAML nao aceitam front-matter sem quebrar o formato:
                # os metadados vivem no manifesto e no MAPA_DOC_ARQUIVO.
                destino_path.write_text(conteudo, encoding='utf-8')

    manifesto = {
        'lote': LOTE,
        'export': export_dir.name,
        'total_docs': len(docs),
        'ingeridos': sum(1 for d in docs if d['acao'] == 'ingerido'),
        'ponteiros': sum(1 for d in docs if d['acao'] == 'ponteiro'),
        'duplicatas': sum(1 for d in docs if d['acao'] == 'duplicata'),
        'conversas': [{'uuid': c['uuid'], 'nome': c['name'], 'mensagens': len(c['chat_messages']),
                       'created_at': c['created_at']} for c in conversas],
        'design_chats': [{'uuid': c.get('uuid', ''), 'created_at': c.get('created_at', '')} for c in chats],
        'docs': docs,
    }

    if args.dry_run:
        for d in docs:
            print(f"{d['documento_id']:14s} {d['acao']:10s} {d['classificacao']:11s} {d['canonical_home']}")
        print(json.dumps({k: v for k, v in manifesto.items()
                          if k in ('total_docs', 'ingeridos', 'ponteiros', 'duplicatas')}, indent=2))
        return

    man_path = root / '60-dados/10-raw/03-json/EXPORT_CLAUDE_20260913_MANIFEST.json'
    man_path.parent.mkdir(parents=True, exist_ok=True)
    man_path.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    rot = root / '01-master-index/02-taxonomies/ROTEAMENTO_EXPORT_CLAUDE_20260913.csv'
    with rot.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['documento_id', 'nome_arquivo', 'folder_id', 'canonical_home',
                    'classificacao', 'acao', 'duplicata_de', 'sha256', 'tamanho_bytes', 'justificativa'])
        for d in docs:
            w.writerow([d['documento_id'], d['filename'], d['folder_id'], d['canonical_home'],
                        d['classificacao'], d['acao'], d['duplicata_de'], d['sha256'], d['bytes'],
                        d['motivo_rota']])

    # MAPA_DOC_ARQUIVO: append idempotente (remove linhas do lote e regrava)
    mapa = root / '01-master-index/02-taxonomies/MAPA_DOC_ARQUIVO.csv'
    linhas = [r for r in csv.DictReader(mapa.open(encoding='utf-8'))
              if not r['documento_id'].startswith(PREFIXO_ID)]
    campos = ['documento_id', 'classificacao_id', 'sha256', 'caminho_em_disco', 'tamanho_bytes']
    for d in docs:
        linhas.append({'documento_id': d['documento_id'], 'classificacao_id': LOTE,
                       'sha256': d['sha256'], 'caminho_em_disco': d['canonical_home'],
                       'tamanho_bytes': d['bytes']})
    with mapa.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)

    # OUT-59 proveniencia: docs + conversas + design chats
    src = root / '60-dados/90-evidence/OUT-59_SOURCE_REGISTER.csv'
    with src.open(encoding='utf-8') as f:
        rd = csv.DictReader(f)
        campos_src = rd.fieldnames
        linhas_src = [r for r in rd if not r['documento_id'].startswith((PREFIXO_ID, 'CONV-CLX', 'DCHT-CLX'))]
    for d in docs:
        linhas_src.append({'documento_id': d['documento_id'], 'classificacao_id': LOTE,
                           'nome_arquivo': d['filename'], 'caminho_relativo': d['canonical_home'],
                           'sha256': d['sha256'], 'tipo_documental': d['classificacao'],
                           'vezes_citado': '0', 'evidencia_ids': ''})
    for i, c in enumerate(conversas, 1):
        linhas_src.append({'documento_id': f'CONV-CLX-{i:03d}', 'classificacao_id': LOTE,
                           'nome_arquivo': c['name'] or '(sem titulo)',
                           'caminho_relativo': f"{export_dir.name}/conversations-000/conversations.json#{c['uuid']}",
                           'sha256': sha256(c['uuid']), 'tipo_documental': 'conversa',
                           'vezes_citado': '0', 'evidencia_ids': ''})
    for i, c in enumerate(chats, 1):
        linhas_src.append({'documento_id': f'DCHT-CLX-{i:03d}', 'classificacao_id': LOTE,
                           'nome_arquivo': c.get('uuid', f'design-chat-{i}'),
                           'caminho_relativo': f"{export_dir.name}/design_chats-000/design_chats/{c.get('uuid','')}.json",
                           'sha256': sha256(c.get('uuid', str(i))), 'tipo_documental': 'design-chat',
                           'vezes_citado': '0', 'evidencia_ids': ''})
    with src.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=campos_src)
        w.writeheader()
        w.writerows(linhas_src)

    print(f"docs={len(docs)} ingeridos={manifesto['ingeridos']} "
          f"ponteiros={manifesto['ponteiros']} duplicatas={manifesto['duplicatas']} "
          f"conversas={len(conversas)} design_chats={len(chats)}")


if __name__ == '__main__':
    main()
