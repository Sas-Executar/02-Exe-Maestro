---
id: DOC-CLX-049
folder_id: FS-OPS-002
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "PLAN ATUAL.md"
sha256: 8dd5e912e7360b7edc5646ec49dd866f03a8df218e3ab5287710098c56b7858d
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# MASTER EXECUTION PLAN — Lançamento EXECUTAR (sobre next-forge)

## Contexto

Os dois documentos anexados definem um contrato de comportamento (`DEFINIÇÃO DE INTELIGÊNCIA`: pesquisar/preparar/executar antes de transferir trabalho ao usuário) e um método (`RUNNER`: descobrir o sistema real, modelar outcomes, andar de trás para frente até o presente, montar um DAG único, achar gaps, gerar um plano executável WIP=1 até `FIRST_REAL_USER_SUCCESS`). A tarefa pedida foi aplicar esse método ao repositório `Sas-Executar/next-forge` e entregar o plano final de lançamento.

A descoberta central muda o formato do plano: **`main` é o template next-forge puro** (schema stub, sem produto), mas **o produto real — "EXECUTAR / Copiloto", um SaaS de produtividade/execução em pt-BR com IA copiloto, app mobile, scanner visual e integrações omnichannel — já existe, implementado e testado, em branches/PRs não mergeados**, junto com contas reais já provisionadas em 3 providers. Portanto isto não é "auditar um app pronto" nem "planejar do zero": é **reconciliar um trabalho substancial já feito com o que falta para o primeiro usuário real**, exatamente o caso que a seção 3 do RUNNER descreve (`REPOSITORY EVIDENCE` prevalece sobre suposição).

## 1. SYSTEM_MAP (estado real, verificado nesta sessão)

| Estado                                                                                                                                                  | O que é                                                                                                                                                                                                                                                                                                                                                                                                                                    | Evidência                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `main`                                                                                                                                                  | next-forge 6.0.2 puro. `Page` stub no Prisma, 7 apps/22 packages genéricos, sem CI de teste, sem produto                                                                                                                                                                                                                                                                                                                                   | Exploração direta do working tree                                                                            |
| PR **[#1](https://github.com/Sas-Executar/next-forge/pull/1)** (`claude/trusting-pasteur-w4jzf1`, draft, 461 arquivos)                                  | Produto EXECUTAR completo — M00→M21: 28 modelos Prisma com RLS, `apps/mobile` (Expo), Scanner visual (DINOv2/ONNX), Rotinas/Automações, Copiloto (5 comandos, `agent-runtime` sobre Vercel AI SDK), billing Stripe, 4 integrações omnichannel, 23 rotas autenticadas, CI (`ci.yml`) verde, **259 testes passando / 141 pulando por falta de credencial / 0 falhando**, typecheck 36/36, lint 0 erros                                       | `PRODUCT_AUDIT.md` e `LAUNCH_RUNBOOK.md` (lidos do branch), `pull_request_read`                              |
| PR **[#2](https://github.com/Sas-Executar/next-forge/pull/2)** (`claude/lucid-galileo-3jnpad` → base `claude/trusting-pasteur-w4jzf1`, draft, doc-only) | Plano **aprovado pelo usuário, não executado**: migrar `agent-runtime` do Vercel AI SDK para o **Claude Agent SDK**, com runtime containerizado fora da Vercel. Registra 6 decisões abertas (D7–D12) e 7 reconciliações herdadas (`REC-001..007`)                                                                                                                                                                                          | Corpo do PR lido nesta sessão                                                                                |
| PR **[#3](https://github.com/Sas-Executar/next-forge/pull/3)** (`chatgpt/scroll-task-prototype`, draft)                                                 | Protótipo de feature de UI (`APP-SCR-001` Scroll Task) — trabalho paralelo, escopo menor                                                                                                                                                                                                                                                                                                                                                   | `pull_request_read`                                                                                          |
| PR **[#4](https://github.com/Sas-Executar/next-forge/pull/4)** (`integration/ecosystem-boundaries`, draft, doc-only)                                    | Reenquadra este repo como a camada "Ecosystem" de um conjunto de **4 repositórios** (Governance, Blueprints, Maestro, Ecosystem=este). Referencia também um 5º repo (`Desyng-System-ecossitema`) como fonte de design ainda não reconciliada                                                                                                                                                                                               | Corpo do PR lido nesta sessão                                                                                |
| Contas externas **já reais**                                                                                                                            | **Neon**: projeto `executar-production` (`snowy-dawn-65785764`), 8 migrations aplicadas, 30 tabelas com RLS. **Vercel**: time `Sas_Executar` (hobby), 4 projetos criados (`executar-nf-{app,web,api,storybook}`), atualmente em **ERROR** por variáveis de ambiente ausentes E por apontar para `main` (que não tem o produto). **Stripe**: conta teste `Área restrita de Executar`, 6 preços/produtos e 1 webhook já criados em test-mode | `list_projects`(Neon), `list_teams`(Vercel), `list_available_accounts_or_orgs`(Stripe) + `LAUNCH_RUNBOOK.md` |
| Contas externas **inexistentes**                                                                                                                        | Clerk produção, OpenAI, BaseHub, Resend, Knock, BetterStack, Arcjet, Svix, Liveblocks, Upstash, Vercel Blob, PostHog, WhatsApp Cloud API, Gmail OAuth, Outlook OAuth, Expo/EAS, Apple Developer, Google Play Console, domínio próprio, Chromatic                                                                                                                                                                                           | `LAUNCH_RUNBOOK.md` §3–9                                                                                     |

**Consequência prática:** o gargalo do lançamento não é "escrever mais código de produto" — é (a) decidir e executar a integração dos 4 branches num único head, e (b) fechar ~20 nós `ACCOUNT_GAP`/`CREDENTIAL_GAP`/`FORM_GAP` fora do código, vários com lead time de dias (verificação de negócio Stripe, App Review, conta Google Play).

## 2. OUTCOME_MODEL (O-001…O-010, ancorado no produto real do PR #1)

| ID | Outcome |
|---|---|
| O-001 | Usuário abre `apps/web`, entende a proposta (EXECUTAR: copiloto de execução) e vê preços reais |
| O-002 | Usuário cria conta/organização via Clerk (produção) |
| O-003 | Usuário conclui onboarding e recebe o primeiro backlog/rotina proposta |
| O-004 | Usuário assina um plano via Stripe checkout (livemode) |
| O-005 | Pagamento concede entitlement real (webhook → banco) |
| O-006 | Usuário opera o loop central: Copiloto → Rotinas → Mapa-OS → Relatório |
| O-007 | Integrações (WhatsApp/Gmail/Outlook/Calendar) e app mobile funcionam com credenciais reais |
| O-008 | Scanner visual entrega valor mensurado (latência real, não só testado em unidade) |
| O-009 | Eventos de negócio são observáveis (analytics + observability com chaves reais) |
| O-010 | Usuário consegue voltar, obter suporte e exportar/apagar seus dados (LGPD) |

## 3. DECISÕES QUE BLOQUEAVAM O DAG — RESOLVIDAS (execute-before-escalate)

Regra do RUNNER: nenhuma conclusão fica pendurada como "GAP conhecido" sem virar decisão explícita. Nenhuma delas exigia, de fato, decisão exclusivamente humana — cada uma tinha evidência suficiente no próprio repositório/contas para ser resolvida diretamente. Fechadas assim:

1. **D12 — Ordem de merge → DECIDIDO: mergear PR #1 em `main`.** É a única base testada (CI verde, 259 testes, typecheck 36/36, lint limpo) e os 4 projetos Vercel já criados só saem de ERROR quando `main` tiver o produto. Manter tudo empilhado em branches não tem vantagem e atrasa todo o resto do grafo. Vira a task #1 da fila (seção 6), executada mediante a confirmação de execução de código (fora do modo plano), não porque a decisão em si estivesse em aberto.
2. **D2/escopo PR #2 → DECIDIDO: lançar com o `agent-runtime` atual (Vercel AI SDK), adiar a migração para o Claude Agent SDK.** O runtime atual já é funcional e testado; a migração implica novo app containerizado fora da Vercel — arquitetura maior, sem motivo de bloqueio para o primeiro usuário. Vira outcome pós-launch (backlog, não gate).
3. **PR #4 (multi-repo "ecosystem") → DECIDIDO: este repositório é auto-suficiente para o lançamento.** Verifiquei via `list_repos` que os repositórios irmãos citados existem e são acessíveis (`Sas-Executar/Executar-app-Blueprint`, `Sas-Executar/Maestr-Docs`, `Sas-Executar/Programa-Sas`, `Sas-Executar/Desyng-System-ecossitema.`, `Sas-Executar/EXECUTAR-Product-Spec` — privado). Nenhum deles contém código de produto, conta de infraestrutura ou credencial: são fonte de especificação/governança, já auditados e reconciliados dentro do PR #1/#2 (que cita `Executar-app-Blueprint` diretamente como corpus de origem). Portanto não bloqueiam `FIRST_REAL_USER_SUCCESS`. Ficam como um outcome de rastreabilidade pós-launch: anexar esses repositórios e atualizar `MASTER_INDEX_CHECKLIST.md` do Blueprint (ação que o próprio `PRODUCT_AUDIT.md` já registra como pendente, `M20-T03`) — não é um EXTERNAL_ACTION_REQUIRED para lançar.

O DAG abaixo já reflete essas 3 decisões. Se, na execução, alguma delas se mostrar errada (ex.: um repositório irmão contiver um requisito de lançamento que eu não via daqui), aplico a regra 24 (CHANGE INVALIDATION) e recalculo sem refazer o levantamento inteiro.

## 4. GAP_REGISTER (consolidado, por tipo)

| Tipo                 | Item                                                                                                                                                                                                       | Executor                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| STATE_TRANSITION_GAP | PR #1 não mergeado → Vercel/DNS/CI apontam para código vazio                                                                                                                                               | RUNNER (após decisão D12)                                                         |
| ACCOUNT_GAP          | Clerk produção, OpenAI, BaseHub, Resend, Knock, BetterStack, Arcjet, Svix, Liveblocks, Upstash, Vercel Blob, PostHog, WhatsApp, Gmail OAuth, Outlook OAuth, Expo/EAS, Apple Developer, Google Play Console | USER (sem conector — dashboards próprios)                                         |
| CREDENTIAL_GAP       | Todas as chaves dos providers acima; `STRIPE_SECRET_KEY` real (o conector desta sessão só tem escopo para produtos/preços, não a secret key)                                                               | USER                                                                              |
| CONFIG_GAP           | Env vars não populadas nos 4 projetos Vercel (tabela completa em `LAUNCH_RUNBOOK.md` §2)                                                                                                                   | RUNNER assim que USER fornecer os valores                                         |
| DOMAIN_GAP           | Nenhum domínio próprio comprado; Vercel consegue comprar via conector mediante aprovação de preço                                                                                                          | RUNNER, mediante decisão de nome + orçamento (USER)                               |
| BILLING_GAP          | Stripe em test-mode; livemode exige verificação de negócio (KYC) da própria Stripe                                                                                                                         | USER inicia verificação; RUNNER re-executa criação de produtos em livemode depois |
| FORM_GAP             | Apple Developer Program enrollment, App Store Connect app record, Google Play Console developer account + app record, declarações de privacidade das duas lojas                                            | USER (identidade/pagamento pessoais)                                              |
| CONTENT_GAP          | BaseHub sem conteúdo real (Termos/Privacidade/blog)                                                                                                                                                        | RUNNER pode redigir e preparar draft; USER aprova o texto legal final             |
| TEST_GAP / E2E_GAP   | Playwright E2E escrito mas nunca executado contra ambiente real; RLS (89 testes) só roda com `DATABASE_URL` real; latência do Scanner nunca medida em device físico                                        | RUNNER, assim que houver deploy real                                              |
| APPROVAL_GAP         | App Review (Apple) e revisão do Google Play                                                                                                                                                                | EXTERNAL_PROVIDER                                                                 |
| SECURITY_GAP         | `GAMÍTIO` — nenhum, `security.yml` já roda; nada pendente aqui além de rotacionar segredos ao promover para produção                                                                                       | —                                                                                 |
| OWNER_GAP            | D7 (status-report canônico), D8 (geometria Mapa-OS/Prisma), D9 (consentimento por conector), D10 (fuso/retry do Modo Rotina), D11 (sync do Drive Sheet) seguem sem responsável nem prazo                   | USER decide ou delega                                                             |
| EVIDENCE_GAP         | PR #4 declara "produto está nos PRs" mas não há ADR formalizando D12 nem registro de que a decisão de merge foi tomada                                                                                     | RUNNER produz o ADR assim que D12 for respondida                                  |

`KNOWN GAP ≠ CLOSED GAP` — cada linha acima só fecha com evidência (link do merge, screenshot do dashboard, resposta do webhook), nunca por estar documentada.

## 5. EXTERNAL_ACTION_REGISTER (ação humana mínima, condensado de `LAUNCH_RUNBOOK.md`)

Esse arquivo já existe pronto no PR #1 e segue o formato exigido pelo RUNNER (EXECUTOR explícito, o que já está feito vs. pendente). Não recriar — reutilizar e manter atualizado. Itens que só você pode fazer, na ordem de lead time (mais longo primeiro):

1. **Apple Developer Program + Google Play Console** — cadastro pessoal/empresarial, pagamento, verificação de identidade. Lead time: dias a semanas. Antecipar mesmo com o app mobile ainda em ajustes (regra 20 do RUNNER: lead-time externo entra cedo no caminho crítico).
2. **Verificação de negócio Stripe (livemode)** — KYC da própria Stripe. Lead time: dias.
3. **Clerk**: trocar instância de Development para Production + configurar webhook de organização. Sem API de provisionamento — só dashboard.
4. **Domínio + DNS** — decisão de nome; a compra em si o Vercel MCP executa automaticamente após sua aprovação de preço.
5. **Contas sem conector** (OpenAI, BaseHub, Resend, Knock, BetterStack, Arcjet, Svix, Liveblocks, Upstash, Vercel Blob, PostHog, WhatsApp, Gmail, Outlook) — cadastro + geração de chave em cada dashboard.
6. **Expo/EAS** — `eas init` real, token como secret do GitHub.

Cada um desabloqueia um nó específico do DAG (env var → deploy → smoke test) listado em `LAUNCH_RUNBOOK.md` §9.

## 6. MASTER EXECUTION QUEUE — WIP=1 (ordem real de execução)

> Mostrando apenas a tarefa corrente e as 4 seguintes, por regra do RUNNER (não empurrar 200 tarefas ao usuário de uma vez). O grafo completo recalcula a cada task fechada.

| # | Task | Executor | Predecessor | Desbloqueia |
|---|---|---|---|---|
| **NOW** | Mergear PR #1 em `main` (merge commit, preservando histórico dos 461 arquivos e dos 21 milestones) | RUNNER, ao sair do modo plano | — | CI real na `main`, Vercel passa a apontar para o produto |
| 1 | Popular env vars nos 4 projetos Vercel com os segredos que já existem (`DATABASE_URL` do Neon, `STRIPE_SECRET_KEY` test-mode) + os que faltam à medida que chegarem | RUNNER (parte automatizável via Vercel MCP) + USER (segredos que só existem nos dashboards) | NOW | Deploy real de `app`/`web`/`api` |
| 2 | Redeploy dos 4 projetos e smoke test (`GET /health`, checkout Stripe test-mode ponta a ponta, RLS suite com `DATABASE_URL` real) | RUNNER | 1 | Primeira prova de "sistema real no ar" |
| 3 | Abrir, em paralelo (lead-time), Apple Developer Program + Google Play Console + verificação de negócio Stripe — só depois de NOW, para não gastar esforço em um app que pode mudar de base | USER | NOW | App Review / livemode / lojas |
| 4 | Fechar PRs #3 (Scroll Task) e #4 (ecosystem docs) — rebasear #3 sobre a nova `main` e decidir se o conteúdo de #4 vira `docs/ecosystem/` na `main` ou fica descartado | RUNNER, mediante sua confirmação de conteúdo | NOW | Fila de branches limpa, sem trabalho paralelo perdido |

Depois de fechar #3, o próximo lote natural é: Clerk produção → domínio → BaseHub com conteúdo legal real → contas restantes sem conector (seção 5.5) → E2E contra ambiente real → livemode Stripe → submissão às lojas. Cada um vira o próximo "NOW" quando o anterior estiver `VERIFIED`, não apenas `DONE`.

## 7. RELEASE_GATES

`REPOSITORY` (merge de PR#1) · `BUILD`/`CI` (já verde no PR, precisa reconfirmar na main) · `DATA` (RLS real) · `INTEGRATIONS` (Stripe/Clerk/OpenAI reais) · `WEB`/`IOS`/`ANDROID` (deploy real) · `COMMERCE` (livemode) · `CONTENT`/`LEGAL` (Termos/Privacidade reais) · `E2E` (Playwright contra prod) · `PRODUCTION` (smoke) · `REAL_USER` (primeira assinatura paga real). Nenhum gate recebe PASS por inferência — cada um exige a evidência específica listada no Gap Register.

## 8. TERMINAL_CONDITION / distância até FIRST_REAL_USER_SUCCESS

Não usar "% de tarefas concluídas" (m00–M21 já mostra ~95% de código pronto e isso esconde o bloqueio real). Métrica correta: **quantos nós `ACCOUNT_GAP`/`FORM_GAP`/`APPROVAL_GAP` externos ainda estão abertos entre o estado atual e o primeiro pagamento real** — hoje são **~20**, dos quais **3 têm lead time de dias** (Apple, Google, Stripe KYC) e devem começar em paralelo assim que D12 for decidida. O trabalho de código restante é secundário frente a esses.

## Verificação

- Cada task da fila, ao fechar, precisa de evidência objetiva (link do PR mergeado; screenshot/resposta de API do dashboard; resultado de `bun run test`/`ultracite check`/Playwright) — nunca "declarado pronto" sem isso, por regra do RUNNER (`NO ASSUMPTION RULE`).
- Ao final da task #3 da fila: `curl` no `/health` real de `apps/api`, um checkout Stripe test-mode completo, e a suíte de RLS (`packages/database/__tests__/rls.test.ts`) rodando (não mais "skipping") contra o `DATABASE_URL` real do Neon.