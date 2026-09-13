---
id: DOC-CLX-041
folder_id: FS-DAT-009
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "schema-runbook.md"
sha256: 4f89b563139ef950be318bc86192d3af0e24edbe592becaa07565529265c0de2
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# Schema — Runbook único (`ExCa-RUNBOOK-02`)

Entrada: o JSON granular de `ExCa-DADOS-01`. Saída: um único documento Markdown
lido tanto por humano quanto por agente de IA — nunca dois documentos
separados para as duas audiências.

## Estrutura fixa

1. **Sumário Executivo** — 3-6 frases, o que é o plano e o estado atual.
2. **Índice de Navegação** — links para cada seção abaixo, no topo do
   documento (leitura rápida por humano).
3. **Como Usar Este Documento** — duas subseções:
   - Para Humano: como ler, o que pular.
   - Para Agente de IA: como referenciar IDs sem inferir conteúdo não
     declarado (aponta para o Apêndice A).
4. **Por fase/semana** (S0, S1, S2...), cada uma seguindo o padrão de runbook:
   **Propósito → Pré-requisitos → Procedimento → Verificação →
   Troubleshooting → Escalonamento**.
5. **Apêndice A — Schema de IDs** — espelha exatamente os IDs do JSON de
   origem (`S0`–`Sn`, `WB-N` etc.), para que um agente possa citar sem
   reconstruir.

## Regra de honestidade sobre lacunas

Onde o JSON de origem tem campo vazio/ausente (semana pouco detalhada), o
runbook marca `[A detalhar]` explicitamente na seção correspondente. Nunca
preencher com conteúdo plausível — isso vale tanto para leitura humana quanto
para um agente que for consumir o documento depois.

## Formato

Markdown puro, um arquivo (`.md`). Cabeçalhos usam `#`/`##`/`###`
consistentes com o índice do topo (mesmo texto, mesma ordem).
