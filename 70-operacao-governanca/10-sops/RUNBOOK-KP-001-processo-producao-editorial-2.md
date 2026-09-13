---
id: DOC-CLX-043
folder_id: FS-OPS-011
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "RUNBOOK-KP-001-processo-producao-editorial 2.md"
sha256: ca47fcc035f53474c2937051c07fe2a29c121e16d48bee05afc053c14ab9cc4d
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

---
runbook_id: RUNBOOK-KP-001
nome: Processo de Produção Editorial Criativa — Knowledge Pack
status: DEFINITIVO
versao: V2 (recalculada)
substitui: SOP-KP-001-processo-knowledge-pack.md (V1 — continha o módulo de produto misturado à cadeia padrão; corrigido nesta versão)
caso_de_referencia: TP-001 — Fatores de Riscos Cognitivos (executado em 10 sessões/fases, ao longo de 10 dias)
owner: Fundador / Editor
---

# 0. Como este Runbook deve ser lido (contrato de leitura para agentes de IA)

Este documento é executável por um agente de IA em qualquer sessão futura, para qualquer tópico. Regras de parsing:

- Cada tarefa (`T01`…`T26`) é um bloco YAML autocontido, com campos fixos: `id`, `fase`, `depende_de`, `gate_para`, `entrada`, `acao`, `saida`, `criterio_de_gate`, `status`.
- **Regra de dependência dura:** uma tarefa só pode iniciar se todas as tarefas listadas em `depende_de` estiverem com `status: APROVADO`. Se não estiverem, o agente deve interromper e reportar bloqueio — nunca pular a tarefa nem inferir o conteúdo dela.
- **Vocabulário de status controlado:** `PENDENTE` → `EM_ANDAMENTO` → `APROVADO` (gate liberado) | `BLOQUEADO` (falta insumo/evidência/aprovação).
- **Unidade de execução:** cada tarefa corresponde a 1 sessão de trabalho (ciclo 1:1). O processo é executado fase a fase, nunca em lote — foi assim que o caso de referência (TP-001) percorreu as 22 tarefas originais em 10 sessões ao longo de 10 dias. Não comprimir múltiplas tarefas numa única sessão só porque é tecnicamente possível.
- **Placeholders:** `TP-XXX` é o ID do novo pack/campanha; substituir em todos os artefatos ao instanciar o runbook para um novo tópico. `[TÓPICO]` marca conteúdo que muda a cada campanha.
- **Módulo condicional (Seção 7):** existe um bloco de tarefas (`MC-01.x`) que **não faz parte da cadeia padrão**. Ele só é ativado se, durante `T16` (Content-Spec) ou na definição do CTA, ficar claro que o pack vai gerar uma ferramenta/solução própria. Fora dessa condição, ele é ignorado e a cadeia segue direto `T15 → T16`.

---

# 1. Resumo Executivo

Este runbook formaliza, como padrão definitivo, o processo de produção editorial criativa usado para transformar um problema em um Knowledge Pack completo (conteúdo, visual, audiovisual, derivados, QA, operação e aprendizado), aplicável a qualquer tópico futuro, não apenas ao caso de origem.

O processo foi originalmente executado no ciclo **TP-001 — Fatores de Riscos Cognitivos**, ao longo de **10 sessões de trabalho (fase a fase)**, e documentado como 22 "Tarefas" numeradas. Ao recalcular essa numeração para uso genérico, duas correções foram feitas:

1. **Separação do módulo de produto.** No TP-001, as Tarefas 16 a 21 originais (Matriz Fator→Sentido→Solução, PRD, FRD, UX, Agent Spec, Tech Spec, ADR, Data Spec, NFR, Safety Spec, catálogo de perguntas, algoritmo de classificação, output spec e catálogo de intervenções do produto **RC-SOLUTION-001 — Scanner**) surgiram no meio da cadeia editorial como uma **exceção** — um produto emergiu durante a definição do CTA e foi formalizado ali mesmo. Isso não deve ser tratado como etapa padrão. Neste runbook, esse bloco foi extraído para a **Seção 7 — Módulo Condicional MC-01**, ativado apenas quando um pack realmente gerar uma ferramenta.
2. **Numeração recalculada da cadeia principal.** Sem o bloco de produto no meio, e com as etapas finais de produção (especificação visual final, infográfico, vídeo, derivados, QA, agendamento, publicação, medição, aprendizado) formalizadas como tarefas numeradas — coisa que no documento original ficava apenas descrita como "cadeia final" em prosa —, a cadeia padrão passa a ter **26 tarefas (T01–T26)**, não 22. As primeiras 15 tarefas (T01–T15) são idênticas em conteúdo às do TP-001; a partir daí a numeração diverge do original porque o produto foi retirado do meio e o fim da cadeia foi tarefa-ficado.

O resultado é um runbook único, sequencial, com gates explícitos entre tarefas, pronto para ser reaplicado a qualquer campanha ou tópico com o mesmo conjunto de etapas, entregáveis e frameworks — e os mesmos resultados.

---

# 2. Mapa MECE do Processo

| Pilar | Tarefas | Resultado do pilar |
|---|---|---|
| 1. Estratégia & Problema | T01–T05 | Problema do pack definido |
| 2. Conhecimento & Evidência | T06–T13 | Knowledge Pack governado (elementos, evidências, claims) |
| 3. Conteúdo Master | T14–T17 | Artigo fundacional produzido |
| 4. Produção Visual & Audiovisual | T18–T20 | Sistema visual e audiovisual aplicado |
| 5. Distribuição | T21 | Derivados especificados |
| 6. QA & Governança | T22 | QA Spec definido |
| 7. Operação | T23–T26 | Cadeia operacional fechada (publicação → medição → aprendizado) |
| **Módulo Condicional** | MC-01.1–MC-01.7 | Solução/ferramenta formalizada (arquitetura, sem código) — **só quando ativado** |

Cadeia final de qualquer pack: **artigo → visuais → infográfico → vídeo → derivados → QA → agendamento → publicação → medição → aprendizado.**

---

# 3. README deste Runbook

**0. SOT.** Este README é o índice canônico do runbook. Consolida a ordem de leitura, os pontos de entrada e as regras de uso.

**1. Para que serve.** Garantir que qualquer novo pack/campanha (`TP-XXX`, qualquer tópico) siga exatamente as mesmas etapas, entregáveis e frameworks que produziram o TP-001, sem reintroduzir a mistura acidental de produto no meio da cadeia editorial.

**2. Como usar em uma nova campanha.**
1. Copiar este runbook, substituir `TP-XXX` pelo ID do novo pack.
2. Preencher a Seção 4 (Master Index) com os artefatos do novo pack, todos com `status: PENDENTE`.
3. Executar `T01` e seguir a cadeia — nunca pular um gate.
4. Só abrir o Módulo Condicional (Seção 7) se um produto/ferramenta realmente emergir.
5. Ao final de `T26`, o pack está encerrado documentalmente (ver checklist na Seção 8).

**3. Relação com os princípios de marca.** A Seção 9 lista os princípios invariantes — parte deles é estrutural (vale para qualquer tópico, de qualquer vertical), parte é específica da linha Risco Cognitivo (vale quando o novo pack pertence a essa linha). A Seção 9 marca claramente qual é qual.

**4. Documento irmão.** O caso de referência completo (TP-001), com todo o conteúdo já preenchido tarefa a tarefa, permanece como exemplo vivo — consultar sempre que uma tarefa deste runbook parecer abstrata demais.

---

# 4. Master Index (template — preencher por campanha)

| # | ID | Tarefa/Módulo | Tipo | Fase | Artefato de saída | Status |
|---|---|---|---|---|---|---|
| 01 | T01 | Transformação | Padrão | Estratégia | `TP-XXX.TRANSFORMATION.V1` | PENDENTE |
| 02 | T02 | Problema canônico | Padrão | Estratégia | `TP-XXX.PROBLEM.V1` | PENDENTE |
| 03 | T03 | Público e contexto | Padrão | Estratégia | `TP-XXX.AUDIENCE_CONTEXT.V1` | PENDENTE |
| 04 | T04 | Perguntas editoriais | Padrão | Estratégia | `TP-XXX.EDITORIAL_QUESTIONS.V1` | PENDENTE |
| 05 | T05 | Tese central | Padrão | Estratégia | `TP-XXX.THESIS.V1` | PENDENTE |
| 06 | T06 | Inventário de elementos canônicos | Padrão | Conhecimento | `TP-XXX.ELEMENT_INVENTORY.V1` | PENDENTE |
| 07 | T07 | Macrogrupos MECE | Padrão | Conhecimento | `TP-XXX.ELEMENT_MECE.V1` | PENDENTE |
| 08 | T08 | Núcleo × aprofundamento | Padrão | Conhecimento | `TP-XXX.CONTENT_SCOPE.V1` | PENDENTE |
| 09 | T09 | Sequência narrativa | Padrão | Conhecimento | `TP-XXX.NARRATIVE_SEQUENCE.V1` | PENDENTE |
| 10 | T10 | Mapa estrutural (outline) | Padrão | Conhecimento | `TP-XXX.ARTICLE_OUTLINE.V1` | PENDENTE |
| 11 | T11 | Mapa argumentativo | Padrão | Conhecimento | `TP-XXX.ARGUMENT_MAP.V1` | PENDENTE |
| 12 | T12 | Matriz de evidências | Padrão | Conhecimento | `TP-XXX.EVIDENCE_MATRIX.V1` | PENDENTE |
| 13 | T13 | Claims autorizados | Padrão | Conhecimento | `TP-XXX.AUTHORIZED_CLAIMS.V1` | PENDENTE |
| 14 | T14 | Storyboard argumentativo | Padrão | Conteúdo Master | `TP-XXX.ARTICLE_STORYBOARD.V1` | PENDENTE |
| 15 | T15 | Brief visual | Padrão | Conteúdo Master | `TP-XXX.VISUAL_BRIEF.V1` | PENDENTE |
| 16 | T16 | Content-Spec | Padrão | Conteúdo Master | `CONTENT-SPEC-TPXXX-V1` | PENDENTE |
| 17 | T17 | Redação do artigo master | Padrão | Conteúdo Master | `ARTICLE-MASTER-TPXXX-V1` | PENDENTE |
| 18 | T18 | Especificação final de produção visual | Padrão | Visual & Audiovisual | `VISUAL-SPEC-TPXXX-V1` | PENDENTE |
| 19 | T19 | Infográfico master | Padrão | Visual & Audiovisual | `INFO-TPXXX-01` | PENDENTE |
| 20 | T20 | Roteiro de vídeo master | Padrão | Visual & Audiovisual | `VID-TPXXX-MASTER-SCRIPT-V1` | PENDENTE |
| 21 | T21 | Derivados | Padrão | Distribuição | `DERIVATIVES-TPXXX-SPEC-V1` | PENDENTE |
| 22 | T22 | QA & Governança | Padrão | QA | `QA-TPXXX-SPEC-V1` | PENDENTE |
| 23 | T23 | Agendamento | Padrão | Operação | `TP-XXX.SCHEDULE.V1` | PENDENTE |
| 24 | T24 | Publicação | Padrão | Operação | `TP-XXX.PUBLICATION.V1` | PENDENTE |
| 25 | T25 | Medição | Padrão | Operação | `TP-XXX.METRICS.V1` | PENDENTE |
| 26 | T26 | Aprendizado | Padrão | Operação | `TP-XXX.LEARNING.V1` | PENDENTE |
| — | MC-01.1–7 | Formalização de Produto/Solução | **Condicional** | (branch após T15) | `RC-SOLUTION-XXX` (bundle) | NÃO ATIVADO |

---

# 5. Cadeia de Tarefas T01 → T26

### T01

```yaml
id: T01
nome: Definir a Transformação
fase: Estratégia & Problema
depende_de: []
gate_para: [T02]
entrada:
  - Tema bruto da nova campanha/pack
acao: >
  Registrar a transformação desejada: o "antes" (percepção ou dificuldade do
  público) e o "depois" (o que a pessoa passa a reconhecer ou fazer ao final
  do pack).
saida:
  artefato: TP-XXX.TRANSFORMATION.V1
  formato: "Frase única, estrutura antes/depois"
criterio_de_gate: >
  Frase aprovada pelo Fundador/Editor. Sem isso, T02 não inicia.
status: PENDENTE
```

### T02

```yaml
id: T02
nome: Definir o Problema Canônico
fase: Estratégia & Problema
depende_de: [T01]
gate_para: [T03]
entrada:
  - TP-XXX.TRANSFORMATION.V1
acao: >
  Escrever uma única frase concreta que descreva a dificuldade real que o
  pack resolve, mantendo o tema como mecanismo e o problema como a
  dificuldade prática do leitor.
saida:
  artefato: TP-XXX.PROBLEM.V1
  formato: "Frase única de problema canônico"
criterio_de_gate: >
  Um problema, um ID canônico. Não avançar sem essa frase registrada como
  DEFINIDO.
status: PENDENTE
```

### T03

```yaml
id: T03
nome: Definir Público e Contexto
fase: Estratégia & Problema
depende_de: [T02]
gate_para: [T04]
entrada:
  - TP-XXX.PROBLEM.V1
acao: >
  Definir o público primário e os contextos de aplicação (ex.: trabalho,
  estudo, rotina, projetos pessoais) em que o problema aparece.
saida:
  artefato: TP-XXX.AUDIENCE_CONTEXT.V1
  formato: "Público primário + lista de contextos"
criterio_de_gate: >
  Público e contextos registrados e aprovados.
status: PENDENTE
```

### T04

```yaml
id: T04
nome: Definir Perguntas Editoriais
fase: Estratégia & Problema
depende_de: [T03]
gate_para: [T05]
entrada:
  - TP-XXX.AUDIENCE_CONTEXT.V1
acao: >
  Definir 1 pergunta central + 4 perguntas editoriais (O quê / Por quê /
  Onde / Como) que o pack precisa responder.
saida:
  artefato: TP-XXX.EDITORIAL_QUESTIONS.V1
  formato: "1 pergunta central + 4 perguntas O quê/Por quê/Onde/Como"
criterio_de_gate: >
  As 5 perguntas aprovadas antes de definir a tese.
status: PENDENTE
```

### T05

```yaml
id: T05
nome: Definir a Tese Central
fase: Estratégia & Problema
depende_de: [T04]
gate_para: [T06]
entrada:
  - TP-XXX.EDITORIAL_QUESTIONS.V1
acao: >
  Escrever a afirmação síntese que orienta todo o pack, mais a regra
  conceitual associada (o "framework" do pack, se houver).
saida:
  artefato: TP-XXX.THESIS.V1
  formato: "Tese central + regra conceitual"
criterio_de_gate: >
  Fecha o Pilar 1 (Estratégia & Problema). Sem tese aprovada, não se abre
  pesquisa de evidências.
status: PENDENTE
```

### T06

```yaml
id: T06
nome: Mapear Inventário de Elementos Canônicos
fase: Conhecimento & Evidência
depende_de: [T05]
gate_para: [T07]
entrada:
  - TP-XXX.THESIS.V1
acao: >
  Congelar a lista completa de elementos/condições que compõem o tema
  (equivalente aos 20 fatores canônicos do TP-001), sem ainda transformá-los
  em argumento.
saida:
  artefato: TP-XXX.ELEMENT_INVENTORY.V1
  formato: "Lista numerada com ID canônico por elemento"
criterio_de_gate: >
  Inventário CONGELADO — nenhum elemento é adicionado ou removido depois
  deste ponto sem decisão explícita de governança.
status: PENDENTE
```

### T07

```yaml
id: T07
nome: Organizar em Macrogrupos MECE
fase: Conhecimento & Evidência
depende_de: [T06]
gate_para: [T08]
entrada:
  - TP-XXX.ELEMENT_INVENTORY.V1
acao: >
  Agrupar o inventário completo em categorias mutuamente exclusivas e
  coletivamente exaustivas (MECE), sem alterar os elementos canônicos.
saida:
  artefato: TP-XXX.ELEMENT_MECE.V1
  formato: "Tabela macrogrupo → função editorial → elementos incluídos"
criterio_de_gate: >
  Cobertura 100% do inventário, sem duplicação entre macrogrupos.
status: PENDENTE
```

### T08

```yaml
id: T08
nome: Definir Núcleo × Aprofundamento
fase: Conhecimento & Evidência
depende_de: [T07]
gate_para: [T09]
entrada:
  - TP-XXX.ELEMENT_MECE.V1
acao: >
  Selecionar o subconjunto de elementos que vai para o artigo principal
  (núcleo); o restante vira camada de aprofundamento reutilizável em
  derivados futuros.
saida:
  artefato: TP-XXX.CONTENT_SCOPE.V1
  formato: "Lista núcleo (com papel no artigo) + lista aprofundamento"
criterio_de_gate: >
  Núcleo aprovado antes de sequenciar a narrativa.
status: PENDENTE
```

### T09

```yaml
id: T09
nome: Definir Sequência Narrativa
fase: Conhecimento & Evidência
depende_de: [T08]
gate_para: [T10]
entrada:
  - TP-XXX.CONTENT_SCOPE.V1
acao: >
  Ordenar os elementos do núcleo em progressão argumentativa — do
  reconhecimento mais imediato até o mecanismo mais sistêmico.
saida:
  artefato: TP-XXX.NARRATIVE_SEQUENCE.V1
  formato: "Ordem numerada + função narrativa de cada elemento + linha
    narrativa condensada"
criterio_de_gate: >
  Sequência aprovada; é a base direta do outline.
status: PENDENTE
```

### T10

```yaml
id: T10
nome: Mapa Estrutural do Artigo (Outline)
fase: Conhecimento & Evidência
depende_de: [T09]
gate_para: [T11]
entrada:
  - TP-XXX.NARRATIVE_SEQUENCE.V1
  - TP-XXX.EDITORIAL_QUESTIONS.V1
acao: >
  Transformar tese + perguntas editoriais + sequência narrativa em títulos e
  subtítulos (H1/H2/H3), sem redigir o artigo ainda.
saida:
  artefato: TP-XXX.ARTICLE_OUTLINE.V1
  formato: "Estrutura H1/H2/H3 completa"
criterio_de_gate: >
  Outline aprovado — nenhuma seção do artigo final pode existir fora dele.
status: PENDENTE
```

### T11

```yaml
id: T11
nome: Mapa Argumentativo
fase: Conhecimento & Evidência
depende_de: [T10]
gate_para: [T12]
entrada:
  - TP-XXX.ARTICLE_OUTLINE.V1
acao: >
  Para cada seção do outline: afirmação → argumento → evidência necessária
  (ainda sem buscar a evidência real).
saida:
  artefato: TP-XXX.ARGUMENT_MAP.V1
  formato: "Afirmação/argumento/evidência necessária por seção"
criterio_de_gate: >
  Toda seção do outline tem uma entrada correspondente no mapa argumentativo.
status: PENDENTE
```

### T12

```yaml
id: T12
nome: Matriz de Evidências
fase: Conhecimento & Evidência
depende_de: [T11]
gate_para: [T13]
entrada:
  - TP-XXX.ARGUMENT_MAP.V1
acao: >
  Para cada afirmação, buscar e vincular fonte prioritária, força da
  evidência e classificação (norma internacional, experimento primário,
  guia técnico oficial, ou constructo do próprio framework).
saida:
  artefato: TP-XXX.EVIDENCE_MATRIX.V1
  formato: "Bloco/afirmação → fonte → força → classificação"
criterio_de_gate: >
  Toda afirmação do mapa argumentativo tem uma linha correspondente na
  matriz de evidências, incluindo os limites do que pode ser afirmado com
  segurança (gate científico).
status: PENDENTE
```

### T13

```yaml
id: T13
nome: Contrato de Claims Autorizados
fase: Conhecimento & Evidência
depende_de: [T12]
gate_para: [T14]
entrada:
  - TP-XXX.EVIDENCE_MATRIX.V1
acao: >
  Congelar exatamente o que o artigo pode afirmar, como deve afirmar, e o
  que não pode ser escrito. Etiquetar cada claim como [E1] evidência
  primária, [E2] norma/guia oficial, [S] síntese sustentada ou [FW]
  constructo proprietário.
saida:
  artefato: TP-XXX.AUTHORIZED_CLAIMS.V1
  formato: "Lista de claims numerados, cada um com redação autorizada,
    base, nível e o que NÃO escrever"
criterio_de_gate: >
  Fecha o Pilar 2 (Conhecimento & Evidência). Nenhuma redação começa sem
  este contrato. Um claim [FW] nunca é reescrito como [E1].
status: PENDENTE
```

### T14

```yaml
id: T14
nome: Storyboard Argumentativo
fase: Conteúdo Master
depende_de: [T13]
gate_para: [T15]
entrada:
  - TP-XXX.ARTICLE_OUTLINE.V1
  - TP-XXX.AUTHORIZED_CLAIMS.V1
acao: >
  Transformar outline + claims autorizados em progressão parágrafo a
  parágrafo (abertura → blocos temáticos → virada conceitual → fechamento
  com CTA), ainda sem redigir a versão final.
saida:
  artefato: TP-XXX.ARTICLE_STORYBOARD.V1
  formato: "Blocos numerados, cada parágrafo com função + claim referenciado"
criterio_de_gate: >
  Estrutura congelada — cada parágrafo tem função e claim definidos antes de
  qualquer geração de visual.
status: PENDENTE
```

### T15

```yaml
id: T15
nome: Brief Visual
fase: Conteúdo Master
depende_de: [T14]
gate_para: [T16]
entrada:
  - TP-XXX.ARTICLE_STORYBOARD.V1
acao: >
  Definir as imagens + infográfico vinculados a cada bloco do storyboard,
  compartilhando um único cenário-base e linguagem gráfica, com composição
  adaptável para os formatos-alvo.
saida:
  artefato: TP-XXX.VISUAL_BRIEF.V1
  formato: "Por visual: função, cena, elementos representados, blocos do
    storyboard cobertos, mensagem visual, deriváveis"
criterio_de_gate: >
  Fecha a parte de pesquisa/planejamento do Pilar 3. Ponto de decisão: aqui
  é onde se avalia se o pack vai gerar um produto/ferramenta — se sim, abrir
  o Módulo Condicional (Seção 7) antes de prosseguir para T16.
status: PENDENTE
```

### T16

```yaml
id: T16
nome: Content-Spec (Contrato de Produção do Artigo)
fase: Conteúdo Master
depende_de: [T15]
gate_para: [T17]
entrada:
  - TP-XXX.ARTICLE_STORYBOARD.V1
  - TP-XXX.VISUAL_BRIEF.V1
  - "RC-SOLUTION-XXX (se o Módulo Condicional foi ativado)"
acao: >
  Para cada bloco do artigo: objetivo → claim autorizado → evidência →
  exemplo → visual relacionado → CTA → limite de linguagem → referência ao
  elemento canônico → referência à solução (se houver). Este documento não
  escreve o artigo; determina o que cada bloco pode afirmar.
saida:
  artefato: CONTENT-SPEC-TPXXX-V1
  formato: "Contrato bloco a bloco, cobrindo 100% do storyboard"
criterio_de_gate: >
  Nenhuma palavra do artigo final é escrita sem este contrato aprovado.
status: PENDENTE
```

### T17

```yaml
id: T17
nome: Redação do Artigo Master
fase: Conteúdo Master
depende_de: [T16]
gate_para: [T18]
entrada:
  - CONTENT-SPEC-TPXXX-V1
acao: >
  Escrever o Knowledge Master seguindo literalmente o Content-Spec, na
  ordem aprovada, sem introduzir claims fora do contrato.
saida:
  artefato: ARTICLE-MASTER-TPXXX-V1
  formato: "Artigo completo"
criterio_de_gate: >
  Quality Gate: elementos do núcleo na ordem aprovada; elemento e
  risco/conclusão permanecem distintos; claims [E1]/[E2] só onde a evidência
  sustenta; constructos [FW] marcados como framework; exemplos cotidianos,
  não diagnósticos; todas as imagens previstas têm função narrativa; existe
  1 CTA primário com destino mensurável; o artigo origina derivados sem
  nova pesquisa. Fecha o Pilar 3.
status: PENDENTE
```

### T18

```yaml
id: T18
nome: Especificação Final de Produção Visual
fase: Produção Visual & Audiovisual
depende_de: [T17]
gate_para: [T19]
entrada:
  - TP-XXX.VISUAL_BRIEF.V1
  - ARTICLE-MASTER-TPXXX-V1
acao: >
  Converter cada entrada do brief visual em especificação final de
  produção: copy (eyebrow/título/subtítulo/labels/callout), hierarquia de
  leitura, descrição de imagem, limites de texto e regras de overflow por
  formato-alvo (16:9, 4:5, 9:16).
saida:
  artefato: VISUAL-SPEC-TPXXX-V1
  formato: "Uma especificação completa por visual (VIS-01…N)"
criterio_de_gate: >
  Toda peça respeita o design system da marca (tipografia, paleta, estilo,
  safe area) antes de qualquer geração de imagem.
status: PENDENTE
```

### T19

```yaml
id: T19
nome: Infográfico Master
fase: Produção Visual & Audiovisual
depende_de: [T18]
gate_para: [T20]
entrada:
  - VISUAL-SPEC-TPXXX-V1
  - ARTICLE-MASTER-TPXXX-V1
acao: >
  Produzir o infográfico que sintetiza a arquitetura do pack (do objetivo ao
  impacto, passando pelos elementos centrais e pela cadeia de controle),
  com a segunda metade mostrando a inversão operacional (identificar →
  controlar → executar → medir → aprender), sempre marcada como arquitetura
  do framework, não como modelo causal cientificamente validado.
saida:
  artefato: INFO-TPXXX-01
  formato: "Infográfico master, versão horizontal + adaptações vertical/mobile"
criterio_de_gate: >
  Infográfico aprovado antes do roteiro de vídeo, que o reutiliza.
status: PENDENTE
```

### T20

```yaml
id: T20
nome: Roteiro de Vídeo Master
fase: Produção Visual & Audiovisual
depende_de: [T19]
gate_para: [T21]
entrada:
  - ARTICLE-MASTER-TPXXX-V1
  - INFO-TPXXX-01
acao: >
  Escrever o roteiro do vídeo master (duração-alvo definida), estrutura:
  Hook → Tese → Definição → elementos centrais → Acúmulo → Framework →
  aplicação manual → CTA.
saida:
  artefato: VID-TPXXX-MASTER-SCRIPT-V1
  formato: "Roteiro completo com marcação de tempo por bloco"
criterio_de_gate: >
  Fecha o Pilar 4 (Produção Visual & Audiovisual). Roteiro aprovado antes de
  especificar derivados.
status: PENDENTE
```

### T21

```yaml
id: T21
nome: Derivados
fase: Distribuição
depende_de: [T20]
gate_para: [T22]
entrada:
  - ARTICLE-MASTER-TPXXX-V1
  - VISUAL-SPEC-TPXXX-V1
  - VID-TPXXX-MASTER-SCRIPT-V1
acao: >
  Especificar carrossel, Reel/Short, Stories, LinkedIn, newsletter,
  checklist e prompt, cada um referenciando explicitamente o bloco do
  storyboard e o visual de origem. Regra central — derivados reutilizam o
  Knowledge Master; não refazem a pesquisa.
saida:
  artefato: DERIVATIVES-TPXXX-SPEC-V1
  formato: "Uma especificação por formato de derivado"
criterio_de_gate: >
  Nenhum derivado introduz claim novo fora do Content-Spec (T16).
status: PENDENTE
```

### T22

```yaml
id: T22
nome: QA & Governança
fase: QA
depende_de: [T21]
gate_para: [T23]
entrada:
  - ARTICLE-MASTER-TPXXX-V1
  - VISUAL-SPEC-TPXXX-V1
  - DERIVATIVES-TPXXX-SPEC-V1
acao: >
  Validar copy (elemento ≠ conclusão automática de risco; framework sempre
  marcado como framework; nenhuma promessa clínica/determinista);
  hierarquia de leitura (o que estou vendo? / qual a ideia principal? / o
  que faço depois?); overflow nos formatos-alvo; acessibilidade (contraste,
  não depender só de cor, leitura linear); rastreabilidade (todo asset
  carrega problem_id, solution_id se houver, evidence_refs, cta_id e
  métrica associada).
saida:
  artefato: QA-TPXXX-SPEC-V1
  formato: "Checklist de QA preenchido, por peça"
criterio_de_gate: >
  Nenhuma peça vai para agendamento sem QA real aprovado.
status: PENDENTE
```

### T23

```yaml
id: T23
nome: Agendamento
fase: Operação
depende_de: [T22]
gate_para: [T24]
entrada:
  - QA-TPXXX-SPEC-V1
acao: >
  Definir calendário de publicação de todas as peças do pack (artigo,
  visuais, infográfico, vídeo, derivados).
saida:
  artefato: TP-XXX.SCHEDULE.V1
  formato: "Calendário com data/peça/canal"
criterio_de_gate: >
  Calendário aprovado antes de publicar.
status: PENDENTE
```

### T24

```yaml
id: T24
nome: Publicação
fase: Operação
depende_de: [T23]
gate_para: [T25]
entrada:
  - TP-XXX.SCHEDULE.V1
acao: >
  Publicar as peças conforme o calendário e registrar as URLs/posts
  resultantes.
saida:
  artefato: TP-XXX.PUBLICATION.V1
  formato: "Lista de URLs/posts publicados"
criterio_de_gate: >
  Toda peça agendada tem URL registrada antes de iniciar medição.
status: PENDENTE
```

### T25

```yaml
id: T25
nome: Medição
fase: Operação
depende_de: [T24]
gate_para: [T26]
entrada:
  - TP-XXX.PUBLICATION.V1
acao: >
  Capturar os KPIs definidos para o pack (ver Seção 9 — Métricas), por
  peça e agregados.
saida:
  artefato: TP-XXX.METRICS.V1
  formato: "Dashboard/registro de métricas por peça e North Star do pack"
criterio_de_gate: >
  Métricas capturadas por um período mínimo definido antes de fechar o
  aprendizado.
status: PENDENTE
```

### T26

```yaml
id: T26
nome: Aprendizado
fase: Operação
depende_de: [T25]
gate_para: []
entrada:
  - TP-XXX.METRICS.V1
acao: >
  Registrar decisões e aprendizados do ciclo (o que funcionou, o que deve
  mudar no próximo pack) sem apagar o histórico de decisões anteriores.
  Atualizar catálogos/claims se necessário, sempre como adição versionada.
saida:
  artefato: TP-XXX.LEARNING.V1
  formato: "Registro de aprendizado, versionado"
criterio_de_gate: >
  Fecha o pack. Ver checklist de Definition of Done (Seção 8).
status: PENDENTE
```

---

# 6. Ponto de Decisão em T15/T16 — Ativar o Módulo Condicional?

Pergunta de decisão, a responder ao final de T15 ou durante T16: **este pack precisa de uma ferramenta/produto próprio como CTA (ex.: scanner, calculadora, agente interativo)?**

- **Não** → seguir direto de T15 para T16. Este é o caminho padrão.
- **Sim** → abrir o Módulo Condicional MC-01 (Seção 7) antes de fechar T16. O produto é formalizado como subprojeto do pack, nunca substitui ou trava a cadeia principal.

---

# 7. Módulo Condicional MC-01 — Formalização de Produto/Solução (exceção, não padrão)

> **Por que este módulo existe separado da cadeia principal:** no TP-001, esse bloco (formalização do Scanner de Fatores de Risco Cognitivo — RC-SOLUTION-001) foi executado como as antigas "Tarefas 16 a 21", no meio da cadeia editorial. Isso funcionou naquele caso, mas foi uma exceção — um produto emergiu durante a definição do CTA e foi formalizado ali mesmo, misturando arquitetura de produto com produção editorial. Para qualquer novo pack, este bloco só entra **se e quando** um produto realmente emergir, e nunca deve ser tratado como etapa obrigatória do fluxo padrão.

```yaml
modulo: MC-01
nome: Formalização de Produto/Solução
tipo: CONDICIONAL
ativa_apos: T15
retorna_para: T16
regra_fixa: >
  Este módulo produz apenas arquitetura, produto e especificação. Nunca
  chega a implementação de código sem uma decisão explícita e separada de
  "ir para engenharia". O produto fica estacionado como subprojeto do
  pack e não pode consumir ou atrasar indefinidamente a cadeia principal.
subtarefas:
  - id: MC-01.1
    nome: Matriz Elemento → Sentido/Canal → Problema → Solução
    depende_de: [T15]
    saida: TP-XXX.ELEMENT_SOLUTION_MATRIX.V1
  - id: MC-01.2
    nome: Especificação-base da solução (equivalente a PRD)
    depende_de: [MC-01.1]
    saida: PRD-RC-SOLUTION-XXX
  - id: MC-01.3
    nome: Requisitos funcionais (FRD) e UX
    depende_de: [MC-01.2]
    saida: [FRD-RC-SOLUTION-XXX, UX-RC-SOLUTION-XXX]
  - id: MC-01.4
    nome: Catálogo de perguntas/inputs da solução
    depende_de: [MC-01.3]
    saida: QUESTION-CATALOG-RC-SOLUTION-XXX
  - id: MC-01.5
    nome: Algoritmo de classificação/priorização
    depende_de: [MC-01.4]
    saida: CLASSIFICATION-ENGINE-RC-SOLUTION-XXX
  - id: MC-01.6
    nome: Output da solução + catálogo de intervenções
    depende_de: [MC-01.5]
    saida: [OUTPUT-SPEC-RC-SOLUTION-XXX, INTERVENTION-CATALOG-RC-SOLUTION-XXX]
  - id: MC-01.7
    nome: Documentação técnica completa (Agent Spec, Tech Spec, ADR, Data
      Spec, NFR, Safety Spec, MVP)
    depende_de: [MC-01.6]
    saida: "Bundle RC-SOLUTION-XXX (arquitetura completa, sem código)"
criterio_de_saida_do_modulo: >
  Todas as subtarefas em status APROVADO. O produto é referenciado no
  Content-Spec (T16) como solução do CTA, e a execução retoma T16 na
  cadeia principal.
status: NÃO ATIVADO
```

---

# 8. Checklist Definitivo (Definition of Done) por Pack

Um pack só é considerado encerrado documentalmente quando todos os itens abaixo estão `APROVADO`:

Estratégia ✓ · Problema ✓ · Transformação ✓ · Contexto ✓ · Perguntas editoriais ✓ · Evidências ✓ · Claims autorizados ✓ · Storyboard ✓ · Brief visual ✓ · Content-Spec ✓ · Artigo ✓ · Especificação visual ✓ · Infográfico ✓ · Vídeo ✓ · Derivados ✓ · QA ✓ · Agendamento ✓ · Publicação ✓ · Medição ✓ · Aprendizado ✓ · (se aplicável) Solução formalizada ✓

Para fechamento **auditável**, anexar sempre: QA real aprovado, calendário/agendamento, URLs publicadas, métricas capturadas, aprendizado registrado.

---

# 9. Princípios de Governança Invariantes

**Estruturais (valem para qualquer tópico/vertical, dentro ou fora da linha Risco Cognitivo):**

| Princípio | Regra |
|---|---|
| Unidade operacional | 1 problema → 1 knowledge pack → 1 solução (se houver) → N assets → distribuição → métricas → aprendizado |
| Classificação de evidência | [E1] evidência primária · [E2] norma/guia oficial · [S] síntese sustentada · [FW] constructo proprietário — um [FW] nunca vira [E1] |
| Regra de IDs | Um conceito → um ID canônico, nunca reatribuído. Todo asset herda `problem_id`, `solution_id`, `evidence_refs`, `cta_id` e métrica |
| Produto emergente | Formalizado via Módulo Condicional (Seção 7); nunca vira etapa padrão nem código sem decisão explícita |
| Aprendizado sem destruição de histórico | Atualizações de catálogo/claim sempre são adições versionadas, nunca substituições silenciosas |
| Derivados | Reutilizam o Knowledge Master; nunca refazem a pesquisa |

**Específicos da linha Risco Cognitivo (reaplicar quando o novo pack pertencer a esta linha; se o pack for de outra vertical, manter a mesma estrutura de raciocínio trocando os rótulos):**

| Princípio | Regra |
|---|---|
| Distinção conceitual central | Fator ≠ Vulnerabilidade ≠ Exposição ≠ Risco |
| Framework mestre da marca | Objetivo → Contexto → Demanda Cognitiva → Vulnerabilidade → Exposição → Risco Cognitivo → Evento → Impacto |

---

# 10. Métricas

| Camada | Funil |
|---|---|
| Conteúdo | `content_seen → tool_used → next_action_completed` |
| Produto (se Módulo Condicional ativado) | `uso_completo → recommendation_used → next_action_completed` |
| Aprendizado | `problema → elemento → solução → uso → resultado → decisão` |

North Star do pack: definir 1 métrica de conteúdo (+ 1 de produto, se houver) já em T01, não depois de T24.

---

# 11. Nomenclatura e Rastreabilidade

- Pack: `TP-XXX`
- Registro de tarefa/gate: `TP-XXX.<NOME_DA_ETAPA>.V<n>`
- Conteúdo: `CONTENT-SPEC-TPXXX-V1` · `ARTICLE-MASTER-TPXXX-V1`
- Visuais: `VIS-01…N` · `VISUAL-SPEC-TPXXX-V1` · Infográfico: `INFO-TPXXX-01`
- Vídeo: `VID-TPXXX-MASTER-SCRIPT-V1` · Derivados: `DERIVATIVES-TPXXX-SPEC-V1`
- QA: `QA-TPXXX-SPEC-V1`
- Produto (se houver): `RC-SOLUTION-XXX` com specs `PRD-`, `FRD-`, `UX-`, `AGENT-SPEC-`, `TECH-SPEC-`, `ADR-`, `DATA-`, `NFR-`, `SAFETY-`, `MVP-` prefixados ao mesmo ID
