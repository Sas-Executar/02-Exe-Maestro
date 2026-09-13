---
id: WF-MAESTRO-INGESTAO-001
folder_id: FS-OPS-003
tipo: workflow
versao: "1.0"
data: 2026-09-13
status: ativo
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# WF · Ingestão governada de acervo externo

Operacionaliza a Regra zero do `AGENT_MAESTRO.md` para qualquer lote externo
(export de conta, pasta de trabalho, ZIP recebido).

## Entrada

Diretório descompactado do lote em `00-dropzone/06-zip/` ou fora do repositório.

## Passos

1. Ler `01-master-index/CENTRAL_CONTROL.csv` (fonte dos Folder IDs).
2. Determinar `what/why/who/where/when/how/output/risk` do lote.
3. Levantar domínios candidatos.
4. Reindexar skills: `bash 80-tecnologia-plataformas/05-gpt/02-agents/maestro/scripts/bootstrap.sh`.
5. Ler os `SKILL.md` das skills candidatas no vendor.
6. Classificar as skills em PRIMARY/SUPPORTING/VALIDATION conforme `config/SKILL_ROUTING.md`.
7. Simular o roteamento sem escrever:
   `python3 .../scripts/ingest_export.py --export <dir> --root . --dry-run`
8. Executar a ingestão (um único `canonical_home` por fato):
   `python3 .../scripts/ingest_export.py --export <dir> --root .`
9. Relacionar cross-domain por link; duplicatas exatas viram relação, nunca cópia.
10. Validar: `python3 .../scripts/validate_governance.py` (deve sair 0).
11. Emitir resumo executivo ≤ 300 palavras em `70-operacao-governanca/09-evidence/`.

## Regras invioláveis

- Conteúdo ≥ 100 KB não é versionado: vira ponteiro em `00-dropzone/08-to-classify/`.
- Dado pessoal nunca entra no repositório: só ponteiro em `98-private-pointers/`.
- Arquivo em pasta sem `folder_id` registrado reprova na regra R1.
- O pipeline é idempotente: reexecutar o mesmo lote não produz diff.

## Fim

Lote encerrado quando o validador sai 0, o manifesto está gravado em
`60-dados/10-raw/03-json/` e a proveniência consta em `OUT-59_SOURCE_REGISTER.csv`.
