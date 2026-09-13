---
id: DOC-CLX-074
folder_id: FS-OPS-007
tipo: documento-importado
status: decisão
origem: export-claude-20260913
origem_filename: "DECISION LOG "
sha256: 8c3c532dbf4e64dd471d4af045545f0b6a7e65c0fb535c5bcf1473a61c33f129
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

RELATÓRIO CONSOLIDADO — GOVERNANÇA, APPLE HIG, PRISMA E ARTEFATOS UI

Document ID: RPT-GOV-PRISMA-HIG-001
Versão: 1.0.0
Data: 2026-09-13
Finalidade: consolidar, em um único documento para agente de IA, todas as decisões tomadas nesta conversa sobre Apple HIG, Chat com Agente de IA, R3 Control Center, governança D01–D23 e contrato Prisma.
Status: CURRENT_CONSOLIDATED_REPORT

0. REGRAS DE LEITURA

Classes usadas:

• OBSERVED: fato observado em fonte, arquivo ou repositório.
• DECISION: decisão explícita aceita.
• PROJECT_RULE: regra interna do projeto.
• PROPOSED: estrutura ou ação ainda não confirmada como executada.
• GAP: lacuna, conflito ou ausência de evidência.
• SUPERSEDED: versão substituída.

Regras obrigatórias:

1. existente ≠ completo ≠ aprovado ≠ implementado ≠ testado ≠ verificado ≠ publicado.
2. Não promover estado sem evidência.
3. ID registrado não equivale a documento concluído.
4. Screenshot, wireframe ou HTML gerado não prova conformidade HIG.
5. O contrato-base Prisma, a projeção Mapa-OS Prisma A4 V4 e o R3 Control Center são coisas distintas.
6. Em conflito, preservar o conflito como GAP.

1. RESUMO EXECUTIVO

A conversa convergiu para quatro decisões principais.

1. Apple HIG como contrato verificável. MST-XP-HIG-TP-001, em D11, tornou-se o template operacional canônico do workflow WF-UI-HIG-CONTRACTS. “Seguir HIG” deixa de ser intenção subjetiva e passa a exigir contrato com ID, severidade, critério verificável, validação, evidência, estado, remediação e exceção.

2. Chat com Agente de IA. D22-DEC-003 mantém a composição canônica do Chat. SPEC-CHAT-AGENT-001 foi corrigida para incorporar Safe Area, targets, Dynamic Type, VoiceOver, Light/Dark, Increase Contrast, Differentiate Without Color, Reduce Motion, localização/RTL, estados assíncronos, componentes nativos e Definition of Done. A correção é documental; implementação e testes não foram confirmados.

3. R3 Control Center. O R3 foi refatorado com princípios HIG para tela e impressão. Ele permanece referência visual de status report, mas não é o contrato Prisma.

4. Prisma canônico. O contrato-base correto foi recuperado: A4 210×297 mm, trim 10 mm, área útil 190×277 mm, três faces 190×92,333 mm, grid de 12 colunas, Header 1–12, Sidebar 1–2, Main 3–12, Footer 1–12, 11 slots por face e semântica Context → Execution → Evidence. Sobre esse contrato foi definido um Content Capacity Contract para controlar tipografia, densidade e overflow por slot.

2. MASTER INDEX

|ID / Artefato                                 |Tipo               |Estado atual                   |Função                         |Próximo passo                |
|----------------------------------------------|-------------------|-------------------------------|-------------------------------|-----------------------------|
|`MST-XP-HIG-TP-001`                           |Template Prompt    |`CANONICAL`                    |Apple HIG UI Contracts         |Aplicar a superfícies reais  |
|`WF-UI-HIG-CONTRACTS`                         |Workflow           |`DEFINED`                      |Auditoria HIG verificável      |Rodar em código/runtime      |
|`D22-DEC-001`                                 |Decisão            |`ACEITA`                       |Padrão canônico de interface   |Continua normativa           |
|`D22-DEC-002`                                 |Decisão            |`ACEITA`                       |Studio / Consultoria           |Continua normativa           |
|`D22-DEC-003`                                 |Decisão            |`ACEITA`                       |Wireframe Chat com Agente de IA|Continua normativa           |
|`SPEC-CHAT-AGENT-001`                         |UI/Product Spec    |`draft_for_pre_approval` v1.0.0|Chat + contratos HIG           |Implementar e testar         |
|`HIG-AUDIT-CHAT-AGENT-001`                    |Auditoria          |`BLOCKED`                      |Gate HIG do Chat               |Requer runtime/teste         |
|`APPLE_HIG_CONTRACT_REGISTRY_CHAT_AGENT.json` |Registry           |`CREATED`                      |Registro de contratos HIG      |Preencher evidência real     |
|`R3_Control_Center_D01-D16_PRISMA_HIG_V3.html`|HTML               |`CURRENT_VISUAL_REFERENCE`     |Status Report R3               |Não usar como contrato Prisma|
|`Prisma One Page · 3 Faces`                   |Contrato           |`CANONICAL`                    |Geometria Prisma               |Preservar shell              |
|`prisma-dashboard-population.template.json`   |Population Contract|`CANONICAL`                    |Slots, prioridades e semântica |Usar como schema             |
|`Mapa-OS Prisma A4 V4`                        |Projeção           |`SEPARATE_PROJECTION`          |Prisma semanal operacional     |Não confundir com base       |
|`GOVERNANCE_PRISMA_CANONICAL_CAPACITY_V3.html`|HTML               |`CURRENT_WORKING_ARTIFACT`     |Governança D01–D23             |Auditar semântica + fit      |
|`Master Governance Registry`                  |Registry           |`PROPOSED / NOT_STARTED`       |Rastreabilidade transversal    |Materializar após aprovação  |
|`RPT-GOV-PRISMA-HIG-001`                      |Relatório          |`CURRENT_CONSOLIDATED_REPORT`  |Handoff desta conversa         |Atualizar em novas decisões  |

3. APPLE HIG UI CONTRACTS

3.1 Identidade

• ID: MST-XP-HIG-TP-001
• Área: D11 — Experiência / Projeto
• Workflow: WF-UI-HIG-CONTRACTS
• Status: TEMPLATE / CANONICAL

3.2 DECISION

Cada regra HIG aplicável deve virar contrato contendo:

contract_id · category · rule · severity · applies_to · source · project_interpretation · validation_method · expected_result · evidence_required · status · remediation · exception_id

Ordem de autoridade:

1. segurança, acessibilidade mandatória, requisitos legais e políticas de distribuição;
2. documentação oficial atual da plataforma;
3. requisito explícito de produto / acceptance criteria;
4. Design System canônico;
5. implementação legada;
6. preferência estética local.

Contratos incorporados: Safe Area, layout adaptativo, target baseline de 44×44 pt quando aplicável a iOS, Dynamic Type, tipografia semântica, cores semânticas, componente nativo primeiro, VoiceOver, Differentiate Without Color, Reduce Motion, Light/Dark, Increase Contrast, localização/RTL, estados transitórios e evidência obrigatória.

3.3 PROJECT_RULE — capacidade de conteúdo

Apple HIG e Fluent não fornecem um número universal de caracteres por componente. A capacidade deve ser calculada por:

geometria → grid → tipografia → line-height → prioridade → máximo de linhas/itens → overflow.

Overflow não deve ser resolvido com redução arbitrária de fonte.

4. CHAT COM AGENTE DE IA

4.1 D22-DEC-003

Estado: ACEITA.

Quatro zonas:

1. Top Utility Bar
2. Conversation Surface
3. Context Suggestions
4. Composer Dock

Prioridade:

Composer > Conversation > Suggestions > Mode Switch > Utilities

Densidade:

• topo: máximo 4 alvos permanentes;
• sugestões: 0–2;
• composer: máximo 5;
• estado vazio de referência: máximo 11;
• sem sugestões: 9.

O limite de 11 é PROJECT_RULE, não HIG.

4.2 Chat × Work

• Chat: perguntas, comandos, consultas e ações rápidas.
• Work: contexto persistente com arquivos, artefatos, projetos, tarefas, Studio e operações prolongadas.

4.3 Studio

Fluxo:

Chat → intenção/briefing → Studio → artefato/protótipo → handoff

Chat pode iniciar Studio, mas não substitui o canvas persistente do Studio.

5. SPEC-CHAT-AGENT-001

Versão: 1.0.0
Status: draft_for_pre_approval

A SPEC foi corrigida para exigir, quando aplicável:

• Safe Area e teclado;
• 44×44 pt em iOS;
• accessibility labels para icon-only;
• Dynamic Type;
• VoiceOver;
• Light/Dark;
• Increase Contrast;
• Differentiate Without Color;
• Reduce Motion;
• localização longa e RTL;
• componentes nativos;
• feedback de estados assíncronos;
• matriz de validação;
• Definition of Done.

Estados:

EMPTY · TYPING · SENDING · STREAMING · TOOL_RUNNING · TOOL_RESULT · WAITING_FOR_USER · ERROR_RETRYABLE · OFFLINE_DEGRADED · CONVERSATION_WITH_ARTIFACT · VOICE_ACTIVE quando suportado · DISABLED quando aplicável

GAP

A SPEC não comprova implementação, teste ou release.

6. HIG-AUDIT-CHAT-AGENT-001

Estado: BLOCKED

Resultado registrado:

• contratos avaliados: 19;
• PASS: 0;
• FAIL: 0;
• REVIEW_REQUIRED: 5;
• BLOCKED: 14;
• exceções aprovadas: 0.

DECISION: screenshot e wireframe provam composição, não conformidade implementada.

7. R3 CONTROL CENTER

7.1 Estado R3

• fonte: 430 tarefas;
• migradas: 430/430;
• áreas com tarefas: 15/16;
• dependências canônicas: 113;
• não resolvidas: 0;
• review queue: 8;
• validação estrutural: PASS;
• publicação final GitHub: PENDENTE.

Distribuição:
D01 0 · D02 2 · D03 13 · D04 4 · D05 41 · D06 9 · D07 5 · D08 7 · D09 1 · D10 30 · D11 15 · D12 182 · D13 101 · D14 5 · D15 7 · D16 8.

Reviews:
D03=3 · D04=4 · D06=1.

DECISION: 100% significa apenas 430/430 tarefas migradas.

7.2 Refatoração HIG

Artefato: R3_Control_Center_D01-D16_PRISMA_HIG_V3.html

Incorporado:

• A4 fixo somente para impressão;
• responsividade em tela;
• safe areas;
• tipografia semântica;
• Light/Dark;
• prefers-contrast;
• prefers-reduced-motion;
• status com texto + símbolo + forma;
• sem dependência apenas de cor;
• separação explícita entre migração validada e publicação pendente.

LIMITATION: o R3 é referência visual, não contrato Prisma.

8. GOVERNANÇA DO REPOSITÓRIO

Repositório observado: Sas-Executar/03-Exe-Governance
Branch observado: claude/plugin-engineer-workflow-klbtix

OBSERVED

Existem 23 áreas de D01 a D23.

D01–D16

• estado: Estruturado, aguardando preenchimento;
• owner: A definir;
• IDs documentais: 31;
• documentos macro: 16;
• tópicos: 48 (T01–T03 por área).

D17–D23

• IDs documentais: 16;
• documentos macro: 7;
• materialização documental desigual.

Total

• IDs documentais: 47;
• documentos macro: 23.

D22

Decisões aceitas:

• D22-DEC-001 — padrão canônico de interface;
• D22-DEC-002 — Studio / Consultoria;
• D22-DEC-003 — Chat com Agente de IA.

DECISION: o one-page de governança não deve virar inventário bruto; deve mostrar sinais de decisão, rastreio e continuidade.

9. CONTRATO PRISMA CANÔNICO

9.1 Geometria

• A4: 210×297 mm;
• margem/trim: 10 mm;
• área útil: 190×277 mm;
• Face 01: 190×92,333 mm;
• Face 02: 190×92,333 mm;
• Face 03: 190×92,333 mm.

9.2 Shell

Cada face:

• Header;
• Sidebar permanente;
• Main;
• Footer.

9.3 Grid

• 12 colunas;
• Header: 1–12;
• Sidebar: 1–2;
• Main: 3–12;
• Footer: 1–12;
• 11 slots por face.

9.4 Face 01 — Context

Pergunta: “Qual é o estado geral deste projeto?”

Slots:
H1 category P1.2 · H2 identity P1.1 · H3 state P1.3 · S1 persistent identification P2.1 · S2 responsibility P2.2 · S3 reserved P2.3 · M1 dominant state P0.1 · M2 context support P0.2 · M3 secondary support P0.3 · F1 traceability P3.1 · F2 reserved P3.2

9.5 Face 02 — Execution

Pergunta: “Qual é a única coisa que precisa ser executada agora?”

Semântica:
S1 canonical position · S2 constraint · S3 reserved · M1 current action · M2 completion criterion · M3 operational support · F1 traceability · F2 reserved

9.6 Face 03 — Evidence

Pergunta: “O que está comprovado e como retorno ao sistema para continuar?”

Semântica:
S1 persistent reference · S2 verification indicator · S3 reserved · M1 evidence state · M2 resume/QRResumeCard quando aplicável · M3 continuation/NextCard · F1 traceability · F2 reserved

10. PRISMA ≠ MAPA-OS PRISMA A4 V4

Não confundir:

Contrato-base Prisma

• A4 210×297;
• trim 10 mm;
• área útil 190×277;
• faces 92,333 mm;
• sidebar 2/12;
• main 10/12;
• semântica Context / Execution / Evidence.

Mapa-OS Prisma A4 V4

Template específico: assets/templates/status-report-prisma-a4-v4.html

• 3 faces de 99 mm;
• Face 01 Épica;
• Face 02 Execução/calendário;
• Face 03 Resultado/entregáveis;
• semântica operacional semanal própria.

SUPERSEDED: usar R3 ou Mapa-OS para definir o contrato-base Prisma foi um erro corrigido.

11. CONTENT CAPACITY CONTRACT

DECISION: o Prisma deve ser preenchido como formulário/schema.

Ordem:

Geometria → Hierarquia → Typography Budget → Content Budget → Overflow Contract → Population

Cada slot deve possuir:

• slot_id;
• função semântica;
• prioridade;
• estilo tipográfico;
• line-height;
• máximo de linhas;
• máximo de itens, quando aplicável;
• required / conditional / reserved;
• comportamento de overflow.

Se exceder capacidade:

1. remover redundância;
2. condensar preservando IDs, estados, quantidades, critérios e evidências;
3. usar slot condicional semanticamente adequado;
4. mover detalhe para outro artefato;
5. se houver perda semântica, retornar erro de fit.

PROIBIDO:

• shrink-to-fit arbitrário;
• cortar informação essencial;
• esconder overflow;
• preencher slot reserved por conveniência;
• elevar detalhe secundário a P0.

12. GOVERNANCE_PRISMA_CANONICAL_CAPACITY_V3

Estado: CURRENT_WORKING_ARTIFACT

Implementado:

• geometria Prisma;
• 12 colunas;
• Sidebar 1–2;
• Main 3–12;
• Header/Footer completos;
• 11 slots por face;
• prioridades nos slots;
• S3 e F2 reservados;
• budgets de linhas/itens;
• auditoria client-side de overflow;
• marca OVERFLOW;
• sem shrink automático;
• reflow em tela pequena;
• Light/Dark;
• Increase Contrast;
• Reduce Motion.

Validação estática confirmou:

• Face 01: H1 H2 H3 S1 S2 S3 M1 M2 M3 F1 F2
• Face 02: H1 H2 H3 S1 S2 S3 M1 M2 M3 F1 F2
• Face 03: H1 H2 H3 S1 S2 S3 M1 M2 M3 F1 F2

GAP

Ainda não comprovado:

• fit visual real;
• inspeção de impressão/PDF;
• conformidade semântica completa com o population schema;
• acessibilidade runtime.

GAP SEMÂNTICO ESPECÍFICO

Na Face 03, M2 é condicional e destinado a resume / QRResumeCard quando aplicável. A V3 usou M2 como indicador de verificação.

Correção recomendada:

• sem mecanismo de resume/QR: deixar M2 vazio / NOT_APPLICABLE;
• manter indicador de verificação em S2;
• manter continuação em M3.

Não declarar V3 plenamente canônica antes dessa correção e das auditorias.

13. MASTER GOVERNANCE REGISTRY

Estado: PROPOSED / NOT_STARTED

Schema mínimo:

AREA_ID · DOC_ID · PATH · TYPE · STATUS · OWNER · SOURCE · NEXT_ACTION

Critérios propostos:

• 100% dos IDs localizáveis;
• path confirmado;
• status explícito;
• owner explícito ou A DEFINIR;
• source canônica;
• nenhuma duplicação tratada como segunda fonte de verdade;
• nenhuma promoção de estado por inferência.

14. MAPA DE SUPERSESSÃO

|Arquivo                                              |Estado                    |Motivo                                      |
|-----------------------------------------------------|--------------------------|--------------------------------------------|
|`GOVERNANCE_CONTROL_D01-D23_PRISMA_HIG.html`         |`SUPERSEDED`              |catálogo bruto                              |
|`GOVERNANCE_PRISMA_D01-D23_APPLE_HIG_REFACTORED.html`|`SUPERSEDED`              |ainda fora do contrato Prisma               |
|`GOVERNANCE_CONTROL_D01-D23_R3_STYLE_ONEPAGE.html`   |`SUPERSEDED`              |confundia R3 com Prisma                     |
|`GOVERNANCE_PRISMA_CANONICAL_D01-D23.html`           |`SUPERSEDED_BY_CAPACITY`  |sem capacity contract                       |
|`GOVERNANCE_PRISMA_CANONICAL_CAPACITY_V2.html`       |`SUPERSEDED_BY_V3`        |slots reservados/semântica corrigidos depois|
|`GOVERNANCE_PRISMA_CANONICAL_CAPACITY_V3.html`       |`CURRENT_WORKING_ARTIFACT`|atual, ainda com gaps de auditoria          |

15. DECISÃO TRANSVERSAL DE DESIGN

Aplicação conjunta:

• Apple HIG: comportamento, adaptação, acessibilidade e previsibilidade;
• Fluent: hierarquia, spacing, densidade e agrupamento;
• Prisma: geometria, slots, prioridades e shell;
• Design System EXECUTAR: tokens e componentes canônicos;
• Content Capacity Contract: orçamento de conteúdo.

Nenhuma camada substitui silenciosamente a outra.

16. GAPS PRIORITÁRIOS

|Prioridade|GAP                                                                |Ação                                        |
|----------|-------------------------------------------------------------------|--------------------------------------------|
|P0        |Face 03 `M2` da V3 não corresponde claramente a resume/QRResumeCard|deixar vazio/NA ou implementar resume válido|
|P0        |auditoria visual de fit não executada                              |renderizar e inspecionar as 3 faces         |
|P0        |inspeção de impressão não executada                                |exportar/inspecionar PDF ou impressão       |
|P1        |Owner D01–D16 = A DEFINIR                                          |decidir ownership                           |
|P1        |Master Governance Registry não materializado                       |criar registry                              |
|P1        |HIG Chat sem runtime/teste                                         |implementar + QA                            |
|P2        |índices documentais podem exigir reconciliação                     |auditar Master Index do repositório         |

17. PRÓXIMO WORKFLOW RECOMENDADO

NEXT 01 — Prisma Semantic + Fit Audit

1. usar prisma-dashboard-population.template.json como schema;
2. validar semantic_class, requiredness, prioridade e variante permitida de cada slot;
3. corrigir Face 03 M2;
4. executar auditoria visual de overflow;
5. validar impressão A4 em 100%;
6. emitir PASS ou BLOCKED;
7. só depois promover o Governance Prisma a canônico.

NEXT 02 — Master Governance Registry

Materializar:
AREA_ID · DOC_ID · PATH · TYPE · STATUS · OWNER · SOURCE · NEXT_ACTION

NEXT 03 — HIG Runtime Validation

Executar WF-UI-HIG-CONTRACTS no Chat real.

18. ESTADO MACHINE-READABLE

```yaml
report_id: RPT-GOV-PRISMA-HIG-001
date: 2026-09-13

canonical_decisions:
  apple_hig_contracts: MST-XP-HIG-TP-001
  interface_standard: D22-DEC-001
  studio: D22-DEC-002
  chat_wireframe: D22-DEC-003

chat:
  spec: SPEC-CHAT-AGENT-001
  spec_version: 1.0.0
  spec_status: draft_for_pre_approval
  hig_audit: BLOCKED
  implementation: NOT_CONFIRMED
  testing: NOT_CONFIRMED
  release: NOT_CONFIRMED

repository_governance:
  repository: Sas-Executar/03-Exe-Governance
  observed_branch: claude/plugin-engineer-workflow-klbtix
  areas: 23
  document_ids: 47
  macro_documents: 23
  d01_d16:
    status: structured_awaiting_population
    owner: A_DEFINIR
    document_ids: 31
    topics: 48
  d17_d23:
    document_ids: 16
    status: registered_mixed_materialization
  d22_decisions_accepted: 3

r3:
  source_tasks: 430
  migrated_tasks: 430
  canonical_dependencies: 113
  unresolved_dependencies: 0
  review_queue: 8
  structural_validation: PASS
  github_final_publication: PENDING
  visual_reference: R3_Control_Center_D01-D16_PRISMA_HIG_V3.html
  defines_prisma_contract: false

prisma:
  base_contract:
    page_mm: [210, 297]
    trim_mm: 10
    usable_mm: [190, 277]
    face_mm: [190, 92.333]
    grid_columns: 12
    header_columns: [1, 12]
    sidebar_columns: [1, 2]
    main_columns: [3, 12]
    footer_columns: [1, 12]
    slots_per_face: 11
  faces:
    FACE-01:
      domain: context
      question: "Qual é o estado geral deste projeto?"
    FACE-02:
      domain: execution
      question: "Qual é a única coisa que precisa ser executada agora?"
    FACE-03:
      domain: evidence
      question: "O que está comprovado e como retorno ao sistema para continuar?"
  capacity_contract:
    active: true
    shrink_to_fit: prohibited
    overflow: explicit_failure_or_condensation
    preserve_semantics: true
  current_artifact: GOVERNANCE_PRISMA_CANONICAL_CAPACITY_V3.html
  current_artifact_status: CURRENT_WORKING_ARTIFACT
  semantic_audit: PENDING
  visual_fit_audit: PENDING
  print_audit: PENDING

master_governance_registry:
  status: PROPOSED_NOT_STARTED
  schema:
    - AREA_ID
    - DOC_ID
    - PATH
    - TYPE
    - STATUS
    - OWNER
    - SOURCE
    - NEXT_ACTION
```

19. REGRA FINAL PARA CONTINUIDADE

Ao continuar:

• não reutilizar versões SUPERSEDED;
• tratar GOVERNANCE_PRISMA_CANONICAL_CAPACITY_V3.html apenas como working artifact;
• usar o contrato-base Prisma e o population schema como autoridades estruturais;
• preservar D22-DEC-001/002/003;
• preservar MST-XP-HIG-TP-001 como contrato HIG;
• não confundir documentação com implementação;
• não declarar Prisma PASS antes de auditoria semântica, visual e de impressão;
• não inventar owners, statuses, paths ou evidências;
• atualizar este relatório ou seu sucessor sempre que uma decisão canônica mudar.