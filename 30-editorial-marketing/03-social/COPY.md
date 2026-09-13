---
id: DOC-CLX-070
folder_id: FS-EDT-004
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "COPY "
sha256: 57d40f7e9cf9335333fb4effafff007aabc318a96914f404b2598ec4dcf6ad50
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

Áreas e tópicos do ecossistema EXECUTAR

Abaixo está a consolidação do Master Index em nível de Área → Tópicos, reduzindo as 59 rotas técnicas para uma estrutura adequada ao preenchimento da copy geral. As áreas derivam diretamente do campo area do índice.

#	Área	Tópicos / superfícies a preencher
01	Workspace	Home do Workspace · orientação inicial · contexto geral · entrada para execução
02	Projetos	Projetos · Projeto individual · Remix multi-projeto · Projetos Mobile
03	Planejamento	Calendário · Overview · Roadmap · Sprint
04	Execução	Agora · Hoje · Amanhã · Ontem · Mapa-OS · Mobile Home · Mapa-OS Mobile
05	Copiloto / Agent	Copiloto · Copiloto Mobile · entrada de prompt · sugestões · respostas · limites · Chat API
06	Automações	Automações · Rotinas · executar agora · status da rotina · Workflows
07	Relatórios	Relatórios · geração de relatório · histórico · Relatórios Mobile
08	Mapa-OS	Projeção operacional · Agora/Próximo/Depois · Prisma 7D · impressão · atualização
09	Scanner	Scanner Web/App* · Scanner Mobile · reconhecimento · símbolos · despacho · desfazer
10	Documentos	Documentos do projeto* · anexos · recursos · vínculos com objetos de trabalho
11	Integrações	Central de integrações · Gmail · Outlook · WhatsApp · conectar · desconectar · estados
12	Busca / Navegação	Busca global · placeholder · filtros · resultados · zero-result
13	Autenticação	Entrar · Criar conta · Entrar Mobile · Criar conta Mobile
14	Configurações	Configurações Mobile · conta · preferências · integrações relacionadas
15	Web Institucional	Home pública · proposta de valor · produto · funcionamento · benefícios · CTAs
16	Pricing / Monetização	Pricing · planos · benefícios por plano · limites · cobrança · CTA comercial
17	Blog / Editorial	Blog · listagem · artigo · categorias · conteúdo · CTA editorial
18	Contato	Página de contato · formulário · motivo de contato · envio · confirmação
19	Legal	Documento legal · termos · privacidade · conteúdo legal dinâmico
20	SEO	Sitemap · Robots · metadata · títulos · descrições · indexação
21	Notificações	Registro de dispositivo · Push · mensagens transacionais · estados
22	MCP	MCP Streamable HTTP · tools · capabilities · mensagens/descritivos para agentes
23	Developer / System	Webhooks · integrações técnicas · estados administrativos
24	System	Health · página não encontrada · loading · erro · sucesso · indisponibilidade

* Documentos do projeto e Scanner Web/App aparecem no plano, mas não foram observados como page.tsx do App no head analisado.

Estrutura de tópicos de copy dentro de cada área

O template granular já trabalha com campos como journey_stage, section, component, copy_slot, propósito, limite recomendado e campo de preenchimento manual. EXECUTAR_COPY_ECOSYSTEM_TEMPLATE.csv Para seu preenchimento, eu organizaria cada uma das 24 áreas pelos seguintes 12 tópicos canônicos de copy:

Tópico	O que você preenche manualmente
01. Nome	Nome oficial da área, tela, recurso ou função
02. Definição	O que é
03. Propósito	Por que existe
04. Valor	Qual resultado entrega ao usuário
05. Como funciona	Explicação curta do funcionamento
06. Título	Headline principal
07. Subtítulo	Contexto/explicação da tela
08. Ações	CTA principal · CTA secundário · comandos
09. Componentes	Cards · campos · filtros · toggles · labels · menus
10. Estados	Vazio · loading · sucesso · erro · bloqueado · confirmação
11. Ajuda	Helper text · orientação · tooltip · instruções
12. Mensagens	Toasts · alertas · confirmações · notificações

Assim, sua matriz manual principal fica conceitualmente:

24 Áreas × 12 tópicos → copy granular → componente → estado → canal.

Exemplo: Execução → Agora → Propósito → Page Header → Subtitle, ou Scanner → Desfazer → Estado → Feedback → Toast. Esse encadeamento é compatível com a granularidade já existente no CSV, que separa seção, componente, slot, estado/variante, propósito e preenchimento manual. EXECUTAR_COPY_ECOSYSTEM_TEMPLATE.csv