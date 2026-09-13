---
id: DOC-CLX-050
folder_id: FS-OPS-002
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "RUNNER · WORKING BACKWARDS LAUNCH ENGINE.md"
sha256: 45424473e4fa12de114a602f88e1971c8e0a9e898e185f0298f05977610ad3a6
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---



RUNNER · WORKING BACKWARDS LAUNCH ENGINE

1. OBJETIVO

Transformar um ecossistema de software existente em um único plano executável, ordenado por dependências, cuja conclusão implique:

FIRST_REAL_USER_SUCCESS

O Runner não deve produzir apenas auditoria, backlog ou checklist.

Ele deve produzir uma cadeia fechada:

DISCOVER→ UNDERSTAND→ BENCHMARK→ DEFINE OUTCOMES→ WORK BACKWARDS→ BUILD DEPENDENCY GRAPH→ DISCOVER GAPS→ GENERATE EXECUTION PLAN→ EXECUTE WIP=1→ VERIFY→ RELEASE→ REAL USER PROOF

  

2. PRINCÍPIO FUNDAMENTAL

O sistema possui um único estado canônico de lançamento.

Não criar planos independentes para:

- código;
- mobile;
- marketing;
- integrações;
- stores;
- formulários;
- infraestrutura;
- conteúdo;
- segurança.

Tudo pertence ao mesmo grafo.

Exemplo:

FEATURE  
→ depende de API  
→ depende de secret  
→ depende de conta externa  
→ depende de formulário  
→ depende de aprovação  
→ depende de deploy  
→ depende de teste  
→ depende de analytics  
→ desbloqueia jornada  
→ desbloqueia usuário.

Se qualquer elemento intermediário estiver ausente, a cadeia está incompleta.

  

3. FASE 0 · CONTRATO E ESQUEMAS

Antes da auditoria, estabelecer objetos canônicos.

NODE

Todo elemento relevante deve virar um NODE.

Tipos possíveis:

- BUSINESS_OUTCOME
- JOURNEY
- ROUTE
- FEATURE
- COMPONENT
- API
- DATA
- AUTH
- INTEGRATION
- AGENT
- MCP
- MOBILE
- INFRA
- ACCOUNT
- CREDENTIAL
- SECRET
- CONFIG
- DOMAIN
- DNS
- FORM
- POLICY
- CONTRACT
- BILLING
- ASSET
- CONTENT
- STORE
- APPROVAL
- TEST
- DEPLOY
- ANALYTICS
- OBSERVABILITY
- SUPPORT
- OPERATIONS

Contrato:

NODE_ID  
TYPE  
NAME  
OBJECTIVE  
BUSINESS_VALUE  
ACTOR  
SOURCE  
STATUS  
EVIDENCE  
DEPENDENCIES  
UNLOCKS  
EXTERNAL_PROVIDER  
OWNER  
GAPS  
TEST  
DONE_CONDITION

  

4. FASE 1 · SYSTEM DISCOVERY

Não começar pelo plano.

Primeiro entender o sistema existente.

Inventariar automaticamente:

- repositórios;
- aplicações;
- packages;
- rotas;
- APIs;
- banco;
- schemas;
- migrations;
- auth;
- middleware;
- serviços;
- integrações;
- SDKs;
- MCPs;
- agentes;
- webhooks;
- jobs;
- cron;
- mobile;
- Expo;
- analytics;
- pagamentos;
- providers;
- secrets referenciados;
- environment variables;
- domínio;
- DNS;
- CI/CD;
- stores;
- páginas;
- conteúdo;
- documentação.

Gerar:

SYSTEM_MAP

Não propor execução antes de completar esta etapa.

  

5. FASE 2 · ROUTE INTELLIGENCE

Descobrir todas as rotas reais.

Para cada rota identificar:

ROUTE_ID

PATH

SURFACE

ACTOR

OBJECTIVE

ENTRY_CONDITION

PRIMARY_ACTION

DATA_READ

DATA_WRITE

APIS

INTEGRATIONS

AUTH

PAYMENT

NEXT_STATE

FAILURE_STATES

ANALYTICS

DEPENDENCIES

BUSINESS_OUTCOME

A rota não deve ser tratada apenas como URL.

Exemplo:

/checkout

não representa apenas uma página.

Representa:

PRODUCT→ AUTH→ /checkout→ PAYMENT_PROVIDER→ WEBHOOK→ ORDER→ ENTITLEMENT→ SUCCESS→ ANALYTICS→ NEXT_ROUTE.

  

6. FASE 3 · WEB RESEARCH & BENCHMARK TRIANGULATION

Somente depois de conhecer o sistema real, pesquisar externamente.

Para cada tecnologia, provider, integração ou canal encontrado:

1. consultar documentação oficial atual;
2. consultar requisitos operacionais atuais;
3. consultar requisitos de produção/publicação;
4. consultar políticas aplicáveis;
5. consultar formulários/declarations necessários;
6. consultar requisitos de conta;
7. consultar requisitos de aprovação;
8. consultar requisitos de teste;
9. utilizar benchmarks de produtos comparáveis para identificar possíveis lacunas de experiência.

Prioridade epistemológica:

REPOSITORY EVIDENCE  
+  
OFFICIAL CURRENT DOCUMENTATION  
+  
BUSINESS OBJECTIVE  
+  
BENCHMARK

Benchmark não substitui documentação oficial.

Benchmark serve para descobrir perguntas ausentes.

Para cada pesquisa registrar:

SOURCE_REF  
SOURCE_TYPE  
PROVIDER  
REQUIREMENT  
CHECKED_AT  
APPLIES_TO  
IMPACT

  

7. TRIANGULAÇÃO

Nenhuma conclusão importante deve depender de uma única perspectiva.

Triangular:

A. INSIDE-OUT

O que o código afirma existir?

B. OUTSIDE-IN

O que provider, plataforma, store ou regulamentação exige?

C. OUTCOME-BACKWARDS

O que precisa acontecer para o usuário atingir o resultado?

Quando A, B e C não coincidirem:

GAP.

  

8. FASE 4 · OUTCOME MODEL

Definir primeiro os resultados finais.

Exemplo:

O-001  
Usuário encontra produto.

O-002  
Usuário cria conta.

O-003  
Usuário conclui onboarding.

O-004  
Usuário paga.

O-005  
Pagamento concede acesso.

O-006  
Usuário executa função central.

O-007  
Integrações necessárias funcionam.

O-008  
Valor é entregue.

O-009  
Evento é observado.

O-010  
Usuário consegue retornar ou obter suporte.

O conjunto deve representar o negócio real encontrado.

  

9. FASE 5 · WORKING BACKWARDS

Para cada outcome:

Perguntar repetidamente:

O que precisa ser verdadeiro imediatamente antes disso?

Continuar até chegar ao estado presente.

Exemplo:

USER USES IOS APP

← app disponível

← App Store release

← App Review accepted

← submission complete

← metadata complete

← privacy declarations complete

← build selected

← production binary uploaded

← production build generated

← signing configured

← app record configured

← developer account available

← mobile implementation valid.

Cada elemento vira NODE.

  

10. FASE 6 · DEPENDENCY GRAPH

Criar um DAG canônico.

Relações permitidas:

- REQUIRES
- BLOCKS
- UNLOCKS
- CALLS
- READS
- WRITES
- TRIGGERS
- REDIRECTS_TO
- AUTHORIZES
- CONFIGURES
- VALIDATES
- OBSERVES
- DEPLOYS_TO
- SUBMITTED_TO
- APPROVED_BY
- PRODUCES

Não utilizar apenas listas.

Toda tarefa precisa saber:

PREDECESSORS

e

SUCCESSORS.

  

11. GAP ENGINE

Pesquisar automaticamente os seguintes gaps:

CODE_GAP

Implementação ausente.

ROUTE_GAP

Rota necessária ausente ou incompleta.

DEPENDENCY_GAP

Dependência necessária não satisfeita.

CONFIG_GAP

Configuração necessária ausente.

ENV_GAP

Environment incompleto.

CREDENTIAL_GAP

Credencial necessária inexistente.

ACCOUNT_GAP

Conta externa necessária inexistente.

BILLING_GAP

Billing necessário não ativado.

FORM_GAP

Formulário/declaration necessário não preenchido.

POLICY_GAP

Política necessária ausente.

CONTRACT_GAP

Contrato/termo necessário pendente.

ASSET_GAP

Screenshot, ícone, imagem ou outro asset requerido ausente.

CONTENT_GAP

Copy, metadata ou conteúdo necessário ausente.

APPROVAL_GAP

Aprovação externa pendente.

STORE_GAP

Requisito de store incompleto.

SECURITY_GAP

Controle de segurança ausente.

PRIVACY_GAP

Requisito de privacidade incompleto.

TEST_GAP

Teste necessário ausente.

E2E_GAP

Cadeia não testada integralmente.

OBSERVABILITY_GAP

Resultado não observável.

SUPPORT_GAP

Fluxo de suporte/recuperação ausente.

OWNER_GAP

Ação necessária sem responsável.

EVIDENCE_GAP

Item declarado pronto sem evidência verificável.

STATE_TRANSITION_GAP

Existe estado inicial e final, mas transição entre ambos não foi implementada.

EXTERNAL_ACTION_GAP

Existe ação necessária fora do código ainda não executada.

Nenhum tipo de gap deve ser ignorado porque não envolve programação.

  

12. EXTERNAL REQUIREMENT EXPANSION

Sempre que uma tecnologia ou provider for encontrado, expandir automaticamente sua cadeia de produção.

Exemplo abstrato:

INTEGRATION DETECTED

→ account?

→ plan/billing?

→ application registration?

→ form?

→ credentials?

→ permissions?

→ verification?

→ webhook?

→ production endpoint?

→ policy?

→ review?

→ sandbox test?

→ production activation?

→ production test?

→ monitoring?

→ support?

O Runner deve descobrir essas etapas usando documentação atual.

  

13. HUMAN ACTION CONTRACT

Toda ação deve possuir:

EXECUTOR

Valores:

RUNNER  
USER  
EXTERNAL_PROVIDER

Exemplo:

Alterar arquivo:  
RUNNER

Informar cartão:  
USER

Aceitar contrato:  
USER

Enviar documento societário:  
USER

App Review:  
EXTERNAL_PROVIDER

Nenhuma intervenção humana pode ficar escondida dentro de uma tarefa técnica.

  

14. FORM REGISTER

Manter registro específico:

FORM_ID

PROVIDER

FORM_NAME

WHY_REQUIRED

TRIGGER

URL_OR_LOCATION

FIELDS_REQUIRED

INPUTS_NEEDED

USER_ACTION

DEPENDENCIES

BLOCKS

STATUS

EVIDENCE

Isso inclui:

- declarations;
- store forms;
- privacy questionnaires;
- Data Safety;
- business verification;
- OAuth verification;
- app review information;
- production-access requests;
- billing registration;
- compliance questionnaires;
- outras exigências encontradas.

Objetivo:

ZERO UNKNOWN FORMS AT LAUNCH.

  

15. EXTERNAL ACTION REGISTER

Registrar separadamente toda obrigação fora do repositório:

EXT_ID

PROVIDER

ACTION

ACCOUNT_REQUIRED

PRECONDITIONS

INPUT_REQUIRED

EXECUTOR

DEPENDENCY

UNLOCKS

STATUS

EVIDENCE

Objetivo:

ZERO HIDDEN EXTERNAL ACTIONS.

  

16. TASK GENERATION

Somente depois de:

DISCOVERY  
+  
RESEARCH  
+  
OUTCOME MODEL  
+  
DAG  
+  
GAP ANALYSIS

gerar tarefas.

Cada TASK deve corresponder a uma mudança de estado objetiva.

Contrato:

TASK_ID

NODE_ID

OBJECTIVE

ACTION

TYPE

CURRENT_STATE

TARGET_STATE

PREDECESSORS

BLOCKS

EXECUTOR

PROVIDER

SOURCE_REFS

INPUTS_REQUIRED

OUTPUT

TEST

EVIDENCE_REQUIRED

DONE_CONDITION

PRIORITY

STATUS

  

17. REGRA DE ATOMICIDADE

Uma tarefa não pode esconder uma cadeia.

PROIBIDO:

Configurar iOS

CORRETO:

Criar/validar App ID

Validar bundle identifier

Configurar signing

Gerar production build

Criar/validar app record

Enviar build

Configurar metadata

Completar privacy declarations

Configurar App Review information

Executar TestFlight

Submeter para Review

etc.

Cada mudança independente deve poder receber:

PASS  
ou  
FAIL.

  

18. SINGLE MASTER PLAN

Deve existir apenas:

MASTER_EXECUTION_GRAPH

Não criar listas paralelas desconectadas.

Web, mobile, infraestrutura, conteúdo e integrações permanecem no mesmo DAG.

Views podem ser diferentes.

Fonte canônica continua única.

  

19. EXECUTION ENGINE · WIP=1

O usuário deve receber somente uma tarefa executável por vez.

Uma TASK pode entrar em:

READY

somente quando:

ALL PREDECESSORS = VERIFIED.

Estados:

DISCOVERED

→ BLOCKED

→ READY

→ IN_PROGRESS

→ VERIFYING

→ VERIFIED

ou

FAILED.

Regra:

WIP = 1.

Enquanto existir tarefa IN_PROGRESS, não iniciar outra tarefa dependente.

Tarefas independentes podem permanecer READY, mas não são apresentadas como tarefa principal até o fechamento da atual.

  

20. NEXT TASK ALGORITHM

Selecionar a próxima tarefa considerando:

1. P0 antes de P1;
2. caminho crítico;
3. maior capacidade de desbloqueio;
4. dependências externas longas antecipadamente;
5. risco;
6. reversibilidade;
7. esforço.

Preferir antecipar ações externas com lead time.

Exemplo:

Se App Review será necessário futuramente, não deixar a criação da conta ou cadastros externos para o final apenas porque o código ainda está sendo desenvolvido.

  

21. EXECUTION ENVELOPE

A cada ciclo mostrar apenas:

NOW

Task atual.

WHY NOW

Por que ela é a próxima no DAG.

INPUT

O que é necessário.

ACTION

O que executar.

EXPECTED RESULT

Estado esperado.

VERIFY

Como validar.

EVIDENCE

O que registrar.

UNLOCKS

Quais nós ficam liberados depois.

Depois do PASS:

fechar task

→ recalcular DAG

→ selecionar próxima READY.

  

22. NO ASSUMPTION RULE

Não considerar:

DOCUMENTED = IMPLEMENTED

IMPLEMENTED = CONFIGURED

CONFIGURED = TESTED

TESTED = VERIFIED

SUBMITTED = APPROVED

APPROVED = RELEASED

RELEASED = USED

PAYMENT = ENTITLEMENT

DEPLOYED = HEALTHY

Cada transição precisa de evidência própria.

  

23. CONTINUOUS RESEARCH

Web Research não ocorre apenas uma vez.

Antes de executar tarefas dependentes de providers externos, verificar se os requisitos continuam atuais.

Especialmente:

- Apple;
- Google;
- Expo;
- Meta;
- Vercel;
- Cloudflare;
- payment providers;
- OAuth providers;
- AI providers;
- outros serviços encontrados.

Registrar:

LAST_VERIFIED_AT.

  

24. CHANGE INVALIDATION

Se uma mudança alterar:

- provider;
- auth;
- dados;
- pagamento;
- permissions;
- mobile;
- arquitetura;
- jornada;

reavaliar os nós dependentes.

Não executar o plano como checklist estático.

O DAG é recalculável.

  

25. RELEASE GATES

Criar gates a partir do grafo real.

No mínimo considerar:

REPOSITORY

BUILD

DATA

SECURITY

INFRASTRUCTURE

INTEGRATIONS

AI/MCP

WEB

IOS

ANDROID

COMMERCE

CONTENT

LEGAL/PRIVACY

ANALYTICS

OBSERVABILITY

SUPPORT

E2E

PRODUCTION

REAL_USER

Gate só recebe PASS quando os nós obrigatórios abaixo dele estiverem VERIFIED.

  

26. TERMINAL CONDITION

O workflow NÃO termina quando:

- backlog = 0;
- código foi mergeado;
- build passou;
- app foi submetido;
- deploy terminou.

Termina quando:

REQUIRED_NODE_OPEN = 0

P0_OPEN = 0

P1_LAUNCH_BLOCKING = 0

UNKNOWN_EXTERNAL_REQUIREMENTS = 0

UNKNOWN_FORMS = 0

REQUIRED_APPROVALS_PENDING = 0

CRITICAL_E2E = PASS

PRODUCTION_SMOKE = PASS

REAL_USER_PROOF = PASS

  

27. DEFINIÇÃO DO RESULTADO

O produto final do Runner é:

ONE SYSTEM MAP

ONE OUTCOME MODEL

ONE DEPENDENCY GRAPH

ONE GAP REGISTER

ONE FORM REGISTER

ONE EXTERNAL ACTION REGISTER

ONE MASTER EXECUTION PLAN

ONE WIP=1 QUEUE

ONE EVIDENCE LEDGER

ONE RELEASE STATE

O usuário não precisa descobrir qual é a próxima pergunta.

O Runner deve transformar o desconhecido em nós, os nós em dependências, as dependências em tarefas e as tarefas em uma sequência finita até produção.

O ponto mais importante é o momento em que o plano é gerado. Eu evitaria criar o “plano final” logo depois de ler o repositório. A sequência correta é:

REPO → ROUTES → CAPABILITIES → PROVIDERS → WEB RESEARCH → REQUIREMENTS → OUTCOMES → WORKING BACKWARDS → DAG → GAPS → MASTER PLAN → WIP=1.

Isso evita um problema frequente: descobrir no meio da execução que existiam tarefas anteriores que nunca entraram no plano.

E existe uma segunda melhoria: antecipar dependências externas pelo lead time, mesmo mantendo WIP=1 para execução principal. Por exemplo, Expo permite construir e enviar o binário, mas a própria documentação deixa claro que o envio técnico não equivale à publicação pública; no iOS ainda há TestFlight/App Store Connect/App Review.  O mesmo vale para requisitos do Google Play que podem bloquear produção antes mesmo do código estar em questão.  Portanto, o grafo precisa saber que determinadas tarefas administrativas devem aparecer cedo no caminho crítico.

A métrica principal do Runner também deve mudar. Em vez de “95% das tarefas concluídas”, ela deve ser distância restante até FIRST_REAL_USER_SUCCESS. Isso impede que 200 tarefas pequenas concluídas escondam um único FORM_GAP, APPROVAL_GAP ou PAYMENT_GAP capaz de bloquear todo o lançamento.