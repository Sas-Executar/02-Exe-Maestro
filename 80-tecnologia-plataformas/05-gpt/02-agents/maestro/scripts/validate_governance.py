#!/usr/bin/env python3
"""Validador de conformidade da governanca documental do ECOSSISTEMA 15-08.

Reexecutavel. Sai com codigo != 0 quando a arquitetura e violada.

Regras verificadas:
  R1  todo documento ingerido esta em pasta com folder_id em CENTRAL_CONTROL.csv;
  R2  .md/.txt ingeridos tem front-matter com id, folder_id, origem e sha256;
  R3  documento_id unico no manifesto e no MAPA_DOC_ARQUIVO;
  R4  um fato = um canonical_home (nenhum sha256 gravado em dois caminhos);
  R5  nenhum dado pessoal do export versionado no repositorio.
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from orchestrator.registry import load_folder_registry  # noqa: E402

ROOT = Path(__file__).resolve().parents[5]
MANIFESTO = ROOT / '60-dados/10-raw/03-json/EXPORT_CLAUDE_20260913_MANIFEST.json'
MAPA = ROOT / '01-master-index/02-taxonomies/MAPA_DOC_ARQUIVO.csv'
CAMPOS_OBRIGATORIOS = ('id', 'folder_id', 'origem', 'sha256')
PADROES_PESSOAIS = (r'login_history', r'maiajoaovinicius', r'"email_address"')

falhas = []


def erro(regra, msg):
    falhas.append(f'{regra}: {msg}')


def main():
    if not MANIFESTO.exists():
        erro('R0', f'manifesto ausente em {MANIFESTO.relative_to(ROOT)}')
        return relatorio()

    manifesto = json.loads(MANIFESTO.read_text(encoding='utf-8'))
    docs = manifesto['docs']
    registrados = {r['path'] for r in load_folder_registry()}

    for d in docs:
        caminho = Path(d['canonical_home'])
        pasta = str(caminho.parent)
        if pasta not in registrados:
            erro('R1', f"{d['documento_id']} em pasta nao registrada: {pasta}")
        if d['acao'] == 'duplicata':
            continue
        arq = ROOT / caminho
        if not arq.exists():
            erro('R1', f"{d['documento_id']}: arquivo ausente em {caminho}")
            continue
        if caminho.suffix in ('.md', '.txt'):
            cabeca = arq.read_text(encoding='utf-8')[:800]
            if not cabeca.startswith('---\n'):
                erro('R2', f"{d['documento_id']}: sem front-matter em {caminho}")
                continue
            for campo in CAMPOS_OBRIGATORIOS:
                if not re.search(rf'^{campo}:', cabeca, flags=re.M):
                    erro('R2', f"{d['documento_id']}: front-matter sem '{campo}' em {caminho}")

    ids = Counter(d['documento_id'] for d in docs)
    for did, n in ids.items():
        if n > 1:
            erro('R3', f'documento_id repetido no manifesto: {did} ({n}x)')

    mapa_ids = Counter(r['documento_id'] for r in csv.DictReader(MAPA.open(encoding='utf-8')))
    for did, n in mapa_ids.items():
        if n > 1:
            erro('R3', f'documento_id repetido em MAPA_DOC_ARQUIVO: {did} ({n}x)')

    homes = {}
    for d in docs:
        if d['acao'] == 'ponteiro':
            continue
        homes.setdefault(d['sha256'], set()).add(d['canonical_home'])
    for h, caminhos in homes.items():
        if len(caminhos) > 1:
            erro('R4', f'sha256 {h[:12]} em multiplos canonical_home: {sorted(caminhos)}')

    versionados = {Path(d['canonical_home']) for d in docs}
    for caminho in sorted(versionados):
        arq = ROOT / caminho
        if not arq.exists():
            continue
        texto = arq.read_text(encoding='utf-8', errors='replace')
        for padrao in PADROES_PESSOAIS:
            if re.search(padrao, texto, flags=re.IGNORECASE):
                erro('R5', f'dado pessoal ({padrao}) versionado em {caminho}')

    return relatorio(len(docs))


def relatorio(total=0):
    if falhas:
        print(f'FALHA · {len(falhas)} violacao(oes) em {total} documentos')
        for f in falhas:
            print(f'  - {f}')
        return 1
    print(f'OK · {total} documentos conformes (R1..R5)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
