# MERGE_NOTES — consolidação de 4 skills em executar-relatorios

Changelog interno para humanos. Não faz parte do contrato executado pela
skill (não é lido por `SKILL.md`).

## Fontes

1. `executar-status-report` — motor base de status report.
2. `executar-status-report-business-pack` — superset de (1) + pacote de
   ~60 templates de negócio.
3. `executar-mapa-os` v1.1.0 — protocolo PRISM de mapa operacional semanal.
4. `deskgo-business-workbook` — motor visual/token Desk&Go.

## Decisões de merge

- **(1) vs (2):** `diff` confirmou que todos os arquivos compartilhados
  (references/00–90, `report.schema.json`, `assets/report.css`,
  `assets/source-reference.html`, scripts, examples, evals) são **byte a
  byte idênticos** entre os dois pacotes, exceto `SKILL.md`. (2) foi usado
  como fonte de verdade para o conteúdo compartilhado; o `SKILL.md` de
  ambos foi descartado em favor do novo roteador único.
- **`references/mapa-os/`** — cópia direta de `executar-mapa-os/references/`
  (architecture-executar, activation-index, source-audit, projections,
  mapa-os-contract, prompts/). Nenhum arquivo continha hex de cor.
- **`references/workbook/`** — cópia direta de
  `deskgo-business-workbook/references/{contrato-workbook,
  placeholder-checkbox, playbook-relatorios, visuais-sob-demanda}.md`.
  Nenhum continha hex de cor (são contrato de marcação/estrutura, não de
  paleta).
- **`references/design-tokens.md`** — reescrito do zero a partir de
  `deskgo-business-workbook/references/token-stack.md`, preservando o
  contrato conceitual (raw → alias → componente, proveniência FONTE/
  DECISAO/LACUNA, contraste ≥4.5:1 texto / ≥3:1 gráfico, "acento é sempre
  presentacional") e removendo todo valor numérico/hex/nome de tema da
  extração antiga.
- **`executar-playbook.extracao.yaml`** — **excluído** do pacote, conforme
  instrução: é dado histórico de extração ligado ao contrato de tokens
  antigo, não à estrutura.
- **`executar-playbook.tokens.json` e `temas.json`** — **excluídos**
  (continham valores concretos). Substituídos por
  `assets/tokens/tokens.schema.json` e `assets/tokens/temas.schema.json`,
  que documentam a forma esperada sem nenhum valor, mais
  `assets/tokens/README.md`.
- **`assets/icon.svg`** (ícone da skill mapa-os antiga, paleta própria) —
  não copiado: não fazia parte da árvore-alvo especificada e não tinha
  função fora do antigo manifest de skill individual.
- **Scripts** — todos os 15 scripts das quatro fontes foram copiados.
  `tokens.py` foi adaptado: `DEFAULT_PATH` agora aponta para
  `assets/tokens/tokens.json` (que não existe ainda) em vez de
  `executar-playbook.tokens.json`; `Tokens.load()` e `Tokens.temas()`
  agora levantam `FileNotFoundError` com mensagem explicando que o arquivo
  aguarda o novo contrato de tokens, em vez de estourar um erro genérico.
  `gerar_wireframe.py` tinha hex literal na folha de estilo do wireframe
  gerado (`#6B6B6B`, `#FFFFFF`, `#EEEEEE`, `#BABABA`, `#343434`,
  `#939393`) — convertidos para `var(--exec-color-*)` com comentário de
  aviso; o wireframe gerado só renderiza cor depois que os tokens reais
  existirem.

## Stripping de design (hex → estrutura)

- `assets/report.css` — todos os hex substituídos por
  `var(--exec-color-*)` com nomes semânticos (surface-shell, ink-title,
  ink-secondary, rule-subtle/default/strong, brand/brand-strong,
  accent-soft/soft-alt/soft-strong etc.), nenhuma declaração de valor.
- `references/40-visual-system.md` e `references/60-print-rules.md` —
  mesma tabela de hex trocada pelos mesmos nomes de variável, com nota
  "A DEFINIR — aguardando contrato de tokens" no topo da seção de cor.
- `assets/source-reference.html` e `examples/report-project.html` —
  CSS embutido idêntico ao de `report.css`; recebeu a mesma substituição
  para manter os três arquivos consistentes entre si.
- `examples/business-pack/template-catalog.html` — paleta própria (9
  valores), mapeada para os mesmos nomes semânticos onde o papel batia
  (ink-title, ink-body, ink-secondary, ink-muted, rule-default/subtle,
  brand, surface-shell).
- `assets/templates/peca-a4.svg` e `assets/templates/relatorio-exemplo.html`
  — usavam a paleta "raw" do antigo stack Executar Playbook. Mapeados 1:1
  para os nomes alias que já existiam no `tokens.json` original (ex.:
  `#0061FE` → `var(--exec-color-brand)`), porque o próprio arquivo já
  trazia um bloco `/* TOKENS:INICIO */…/* TOKENS:FIM */` sincronizado por
  `tokens.py --sincronizar`. O bloco `:root{...}` desse marcador foi
  esvaziado para `/* A DEFINIR */` em vez de virar uma auto-referência
  circular (`--exec-color-brand:var(--exec-color-brand)`), que teria sido
  o resultado de uma substituição ingênua.
- `assets/templates/status-report-prisma-a4-v4.html` — paleta própria
  (sistema neutro "Vercel/Geist-inspired"), já organizada em custom
  properties (`--bg`, `--fg`, `--accent` etc.) declaradas uma vez no
  `:root` e consumidas via `var()` no resto do arquivo. Os valores no
  `:root` foram esvaziados para `/* A DEFINIR */`; um punhado de hex
  hardcoded fora do `:root` (herança de edição manual) foi religado às
  mesmas variáveis. `<meta name="theme-color" content="#ffffff">` virou
  comentário HTML (não há como referenciar uma custom property CSS de
  dentro de um atributo `<meta>`).
  - **Exceção documentada:** `outline:.7mm solid #f00` (linha do estado
    `.overflowing`, um indicador de depuração de overflow de conteúdo, não
    uma escolha de marca) foi **mantido como hex literal**. É convenção
    funcional de erro (vermelho = estouro), não uma decisão de tema.
- `assets/data/fixture-quebrada.svg` — fixture de regressão do validador,
  com 16 defeitos plantados. O defeito `TK001` é especificamente "cor
  literal num atributo de apresentação" — **o hex `#FFFFFF` no `fill` do
  `<rect>` da página foi mantido de propósito**, porque removê-lo apagaria
  o próprio defeito que o validador precisa detectar. O `:root` do mesmo
  arquivo (tokens legítimos usados por outros elementos, não o defeito)
  foi esvaziado normalmente para `/* A DEFINIR */`. Ambas as exceções estão
  comentadas inline no arquivo.

## Coisas que ficaram "A DEFINIR" (checar quando os tokens reais chegarem)

- `assets/report.css` — bloco inteiro de `var(--exec-color-*)` sem
  declaração.
- `references/40-visual-system.md`, seção "## Color".
- `references/60-print-rules.md`, exemplo de `@media print`.
- `assets/source-reference.html`, `examples/report-project.html`,
  `examples/business-pack/template-catalog.html` — CSS embutido.
- `assets/templates/peca-a4.svg`, `assets/templates/relatorio-exemplo.html`
  — bloco `/* TOKENS:INICIO */…/* TOKENS:FIM */`.
- `assets/templates/status-report-prisma-a4-v4.html` — bloco `:root` e o
  comentário no lugar do `<meta name="theme-color">`.
- `assets/data/fixture-quebrada.svg` — bloco `:root` (não o defeito
  `TK001`, que é intencional).
- `scripts/gerar_wireframe.py` — folha de estilo `ESTILO` do wireframe.
- `scripts/tokens.py` — `DEFAULT_PATH`/`TEMAS_PATH` apontam para arquivos
  que ainda não existem (`assets/tokens/tokens.json`,
  `assets/tokens/temas.json`); os schemas em `assets/tokens/` documentam a
  forma esperada.

## Namespacing de examples/evals

- `examples/mapa-os-*` — os 7 arquivos de `executar-mapa-os/examples/`
  prefixados com `mapa-os-` para não colidir com os exemplos do status
  report.
- `evals/mapa-os-cases.jsonl` — `cases.jsonl` de `executar-mapa-os/evals/`
  renomeado (formato JSONL é distinto de `evals.json`, mantidos como dois
  arquivos em vez de mesclados).

## Não copiado

- `executar-playbook.extracao.yaml` (ver acima).
- `assets/icon.svg` do mapa-os (ver acima).
- `requirements.txt` do mapa-os — omitido porque seu único conteúdo é um
  comentário dizendo que não há dependências externas.
- `tests/` do mapa-os (`smoke.py`, `test_activation.py`) e `README.md` do
  mapa-os — não fazem parte da árvore-alvo especificada para esta
  consolidação.

## 2026-09-22/23 — Integração do contrato real de tokens (EXECUTAR-REPORT-PRINT-DS-001 v1.0)

O usuário enviou o contrato de tokens definitivo (paleta Green/Azure/Neutral,
IBM Plex, contrato `@page` A4, componentes de relatório executivo). Esta
rodada substitui os placeholders da rodada anterior pelos valores reais.

### Arquivos adicionados
- `references/200-executive-report-print-contract.md` — contrato completo,
  verbatim (fonte de verdade em prosa).
- `assets/templates/executive-report-a4.html` — implementação de referência
  do contrato, copiada verbatim (já vem com valores concretos, não foi
  stripada).
- `assets/tokens/tokens.json` — camadas raw/alias/componente resolvidas.
  Duas vocabulárias de alias coexistem no mesmo arquivo: `--exec-color-*`
  (report.css, peca-a4.svg, relatorio-exemplo.html, source-reference.html,
  examples/report-project.html, template-catalog.html) e o namespace PRISM
  sem prefixo (`bg`, `fg`, `muted`... — status-report-prisma-a4-v4.html),
  armazenado com prefixo `prism-` só dentro do JSON para não colidir de
  nome com a primeira vocabulário.
- `assets/tokens/tokens.css` — gerado a partir de `tokens.json` (não editar
  à mão); `scripts/render_report.py` agora injeta este arquivo antes de
  `assets/report.css`.
- `assets/tokens/temas.json` — um único tema (`executar`), `overrides: {}`.

### Mapeamento alias -> valor
Toda decisão de mapeamento (FONTE vs DECISAO, com a base de cada uma) está
registrada em `assets/tokens/tokens.json`. Resumo: a maioria dos aliases
`--exec-color-*` já existentes mapeou 1:1 ou por espelhamento direto de um
componente do contrato (ex.: `accent-soft` = `azure-2`, porque
`.card.info { background: azure-2 }` no contrato). Nove aliases continuam
`LACUNA` porque o contrato genuinamente não os cobre — ver
`references/design-tokens.md` § "Lacunas em aberto" para a lista e o porquê
de cada um. Nenhum valor foi inventado para preencher uma lacuna.

### Bug real encontrado e corrigido em `scripts/tokens.py`
`PARES_CONTRASTE` usava nomes com o prefixo `--exec-color-` embutido (ex.:
`"exec-color-ink-body"`), mas a camada `alias` de `tokens.json` guarda os
nomes SEM esse prefixo (`"ink-body"`). Como `relatorio_contraste()` engole
`KeyError`/`ValueError` em silêncio, `--contraste` rodava sem erro e sem
imprimir nada — nenhum par era de fato checado. Corrigido para usar os
nomes corretos; a validação agora roda de verdade (ver achados abaixo).

### Achados de contraste (contrato como está, não corrigidos por conta própria)
`python3 scripts/tokens.py --contraste` agora reporta 4 reprovações reais,
usando os valores exatamente como o contrato define (todos `origem: FONTE`
ou espelhamento direto de um componente do contrato):

- `ink-placeholder` (#959494) sobre `surface-page` (#FFFFFF): 3.03:1,
  abaixo do mínimo de 4.5:1 para texto.
- `brand` (#00BF63) sobre `surface-page`: 2.43:1, abaixo de 4.5:1 — Green 9
  não deveria ser usado como cor de TEXTO; o próprio contrato já reserva
  Green 11 (`brand-strong`, #007A45) para "texto/acento acessível" (§3).
- `ink-inverse` (branco) sobre `brand` (verde): 2.43:1, abaixo de 4.5:1 —
  o padrão `.brand-mark { background: var(--action); color:#fff }` do
  próprio template de impressão fica abaixo do mínimo de texto (aceitável
  como logotipo de uma letra/marca, questionável como texto genérico).
- `rule-strong` (#C5C5C5) sobre `surface-page`: 1.73:1, abaixo do mínimo de
  3:1 para objeto gráfico — não deveria ser usado como contorno de checkbox
  ou campo sem reforço adicional (ex.: preenchimento ou traço mais espesso).

Nenhum desses valores foi alterado — são o contrato exatamente como
enviado. Ficam registrados aqui como achado de validação para decisão do
usuário, não como erro de merge.
