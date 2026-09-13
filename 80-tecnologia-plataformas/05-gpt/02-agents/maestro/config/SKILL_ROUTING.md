---
id: CFG-SKILL-ROUTING-001
folder_id: FS-TEC-030
tipo: matriz-de-habilidades
versao: "1.0"
data: 2026-09-13
status: ativo
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# Maestro · Matriz de Habilidades

Define quais skills especializam cada classe de material antes de qualquer escrita
(`AGENT_MAESTRO.md`, Regra zero, passos 4-6). Vale a restrição do `POLICY.yaml`:
`read_skill_before_apply: true` — nenhuma skill é declarada aplicada sem que o
`SKILL.md` real tenha sido lido no vendor canônico.

## Classificação

- `PRIMARY` — decide a forma do entregável. Uma por material.
- `SUPPORTING` — contribui com técnica ou insumo, não decide.
- `VALIDATION` — verifica o resultado; pode reprovar a escrita.

## Matriz

| Classe do material | PRIMARY | SUPPORTING | VALIDATION | Motivo (objeto · intenção · audiência · risco) |
|---|---|---|---|---|
| Export bruto → estrutura de projeto | `reconstructing-projects` | `cmd-01-pps` | `executar-divisao-tarefas` (`VALIDAR EXECUTAR`) | Acervo não classificado · recuperar o modelo real do projeto · orquestrador · risco de perder proveniência |
| Governança e processo (MD/TXT) | `obsidian-editorial` | `copiloto-executar` | `POLICY.yaml` + `validate_governance.py` | Procedimento repetível · operar a rotina · executor · risco de SOP divergente da prática |
| Dados tabulares (CSV/YAML/JSON/XLSX) | `xlsx` | — | `validate_governance.py` | Estrutura de dados · normalizar e conferir campos · consumidores downstream · risco de schema quebrado |
| Entregáveis visuais (HTML/print) | `executar-design` | `dataviz` | revisão humana | Peça publicável · padronizar identidade · leitor externo · risco de impressão/QR inválidos |
| Documentos binários (DOCX/PDF) | `docx`, `pdf` | — | `validate_governance.py` | Documento formatado · extrair e reancorar conteúdo · leitor final · risco de perda de formatação |
| Metadados pessoais (users, login history) | — | — | **bloqueio R5** | Dado pessoal · nunca versionar · ninguém · risco LGPD; rota obrigatória `98-private-pointers` como ponteiro |

## Registry

`runtime/registry/skills-index.json` é gerado por `scripts/index_skills.py` a partir do
submódulo `anthropic-knowledge-work-plugins` (141 skills, sha256 por `SKILL.md`).
Reindexar sempre que o submódulo mudar:

```bash
bash scripts/bootstrap.sh
```

Se o submódulo não estiver disponível, o índice anterior é mantido e a lacuna é
registrada em `60-dados/90-evidence/OUT-58_GAP_REGISTER.csv`. Skills não presentes
no índice não podem ser declaradas como aplicadas.
