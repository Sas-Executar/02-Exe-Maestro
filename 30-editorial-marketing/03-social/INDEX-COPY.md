---
id: DOC-CLX-071
folder_id: FS-EDT-004
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "INDEX COPY"
sha256: e8854dcd2f9e538f771d75e98c7c8db968777b74eef6dfcd642dcf34a195706c
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

Estratégia 2026 para Copy Transversal · EXECUTAR

A estratégia mais adequada para o seu ecossistema é tratar copy como infraestrutura de produto, não como texto escrito página por página.

A regra central seria:

1 significado canônico → N superfícies → N adaptações contextuais.

Isso é especialmente importante no EXECUTAR porque o mesmo conceito atravessa App, Mobile, Copiloto, Scanner, Mapa-OS, relatórios, notificações, e-mail, WhatsApp, Web institucional e MCP. Seu CSV já possui boa parte da infraestrutura necessária: canonical_copy_key, área, superfície, canal, rota, componente, estado, propósito, locale e status. EXECUTAR_COPY_ECOSYSTEM_TEMPLATE.csv

Modelo recomendado

Camada	Função	Exemplo EXECUTAR
L0 · Vocabulário	Define o significado oficial dos conceitos	Projeto · Entregável · Tarefa · Ação · Evidência
L1 · Intenção	Define o que a mensagem precisa comunicar	criar · concluir · bloquear · aprovar · recuperar
L2 · Copy canônica	Frase-base independente de tela	Criar projeto
L3 · Estado	Adapta a mensagem à situação	vazio · loading · erro · sucesso · bloqueado
L4 · Componente	Adapta à função de UI	heading · button · helper · toast · modal
L5 · Canal	Adapta à superfície	App · Mobile · WhatsApp · Email · MCP
L6 · Contexto/Tom	Modifica sem mudar o significado	orientação · ação · alerta · confirmação
L7 · Locale	Localização linguística	pt-BR · en-US etc.
L8 · Medição	Mede se a copy funcionou	clique · conclusão · erro · abandono

O ponto principal é: não permitir que cada canal invente sua própria linguagem.

Por exemplo, a ação canônica pode ser:

ACTION.PROJECT.CREATE

e então gerar:

App: Criar projeto

Mobile: Criar projeto

Copiloto: Posso criar o projeto a partir dessas informações.

WhatsApp: Criar este projeto?

Toast: Projeto criado.

MCP/tool description: Creates a project in the current workspace.

O formato muda. O significado não.

Essa consistência também tem impacto direto em acessibilidade. A W3C recomenda identificação consistente para funcionalidades equivalentes, porque rótulos diferentes para a mesma função aumentam confusão e erros, especialmente para pessoas com dificuldades cognitivas. 

1. Primeiro: crie o Léxico Canônico

Antes de preencher 547 células individualmente, eu criaria uma camada superior com aproximadamente 50–100 termos fundamentais do EXECUTAR.

Exemplo:

Projeto
Entregável
Tarefa
Ação
Evidência
Agora
Próximo
Depois
Rotina
Workflow
Copiloto
Mapa-OS
Scanner
Bloqueio
Capacidade
Aprovação
Concluir
Replanejar

Cada conceito deve ter:

Nome canônico → definição → verbo associado → termos proibidos/sinônimos → uso correto → uso incorreto.

Isso impede, por exemplo, que uma tela diga finalizar, outra concluir, outra fechar e outra marcar como feito quando todas representam a mesma mutação de domínio.

2. Depois: criar famílias de mensagens transversais

Não começaria pelas 24 áreas.

Começaria pelas mensagens que aparecem em todas elas.

As principais famílias seriam:

ACTION — Criar · Editar · Salvar · Excluir · Concluir · Voltar · Cancelar · Tentar novamente.

STATE — Vazio · Carregando · Disponível · Bloqueado · Concluído · Falhou · Pendente.

FEEDBACK — Sucesso · Erro · Aviso · Confirmação.

NAVIGATION — Abrir · Ver · Voltar · Próximo · Pesquisar · Filtrar.

AUTHORITY — Permitido · Requer aprovação · Requer ação humana · Não permitido.

TIME — Agora · Hoje · Amanhã · Ontem · Próximo · Depois.

EVIDENCE — Adicionar evidência · Evidência registrada · Evidência necessária.

SYSTEM — Offline · Reconectando · Sincronizado · Atualizando.

Depois essas famílias são consumidas pelas áreas.

Isso reduz drasticamente duplicação.

3. Voz única; tom contextual

Em 2026, eu separaria formalmente:

Voice = constante.
Tone = variável.

A voz do EXECUTAR deveria permanecer estável em qualquer canal: curta, concreta, operacional e orientada à próxima ação.

Já o tom muda conforme o estado.

Uma confirmação pode ser neutra:

Projeto criado.

Um erro deve ser instrutivo:

Não foi possível criar o projeto. Revise os campos indicados.

Uma situação que exige intervenção:

Esta ação precisa da sua aprovação para continuar.

A Apple também diferencia voz consistente de tom situacional e recomenda linguagem simples, concisa, acessível e preparada para localização. 

4. Para EXECUTAR: Copy orientada à ação

Eu usaria uma regra forte:

Objeto + estado + próxima ação.

Em vez de:

Ocorreu um problema inesperado.

usar:

O relatório não foi gerado. Tente novamente.

Em vez de:

Não há itens para exibir.

usar:

Nenhuma tarefa está pronta para execução.

E quando necessário:

Nenhuma tarefa está pronta. Revise bloqueios ou planeje a próxima ação.

Isso combina muito melhor com a lógica operacional do produto.

A W3C recomenda exatamente esse tipo de clareza: palavras comuns, instruções explícitas, passos compreensíveis e mensagens que indiquem o que o usuário precisa fazer. 

5. Introduzir Copy Tokens

Você já possui canonical_copy_key. Eu transformaria isso em um sistema efetivo de tokens.

Em vez de:

APP-009.PAGE.PRIMARY_CTA.LABEL

eu começaria a separar significado de localização física.

Exemplo:

ACTION.PROJECT.CREATE
ACTION.PROJECT.DELETE
ACTION.TASK.COMPLETE
STATE.PROJECT.EMPTY
STATE.TASK.BLOCKED
FEEDBACK.PROJECT.CREATED
FEEDBACK.TASK.COMPLETED
AUTHORITY.HUMAN_REQUIRED
NAVIGATION.BACK
NAVIGATION.NEXT
SYSTEM.LOADING
SYSTEM.RETRY

A tela passa a consumir o token.

Então:

/projects
   ↓
ACTION.PROJECT.CREATE
   ↓
pt-BR
   ↓
Criar projeto

Isso é muito mais transversal do que amarrar a copy exclusivamente à rota.

6. AI deve gerar variantes, não criar a verdade

Para 2026, eu colocaria IA na camada de produção, mas não como Source of Truth.

Fluxo:

SIGNIFICADO CANÔNICO
        ↓
COPY MASTER
        ↓
IA gera variantes
   ↓        ↓        ↓
Mobile   Email   WhatsApp
        ↓
Validação automática
        ↓
Revisão humana quando necessária
        ↓
Publicação

A IA pode:

adaptar comprimento; adaptar canal; produzir alternativas A/B; localizar; detectar inconsistência terminológica; verificar tom; detectar mensagens sem próxima ação.

Mas não deveria poder decidir que Tarefa, Ação e Entregável são conceitos equivalentes.

Isso pertence à governança de domínio.

7. Criar quatro classes de Copy

Eu acrescentaria ao CSV um campo:

copy_class

com somente quatro valores:

CANONICAL
TRANSVERSAL
CONTEXTUAL
CHANNEL_SPECIFIC

Exemplo:

Criar projeto → CANONICAL

Tentar novamente → TRANSVERSAL

Nenhuma tarefa está pronta para Agora → CONTEXTUAL

Responda SIM para concluir → CHANNEL_SPECIFIC

Isso resolve rapidamente o que pode ser reutilizado e o que realmente precisa ser escrito individualmente.

8. Não preencher as 547 copies em ordem

Este é o ponto que mais mudaria no seu processo.

Eu não preencheria:

CPY-0001 → CPY-0002 → CPY-0003 → ... CPY-0547.

Faria verticalmente:

FASE 01
Vocabulário canônico
↓
FASE 02
Ações transversais
↓
FASE 03
Estados transversais
↓
FASE 04
Feedback e erros
↓
FASE 05
Navegação
↓
FASE 06
Copy específica das áreas
↓
FASE 07
Web institucional
↓
FASE 08
Adaptação por canal
↓
FASE 09
SEO / localização
↓
FASE 10
Teste + telemetria

Uma vez aprovados Salvar, Cancelar, Criar, Concluir, Voltar, Tentar novamente, Carregando, Bloqueado, etc., dezenas de slots deixam de precisar de redação manual.

9. Arquitetura final que recomendo

Para o EXECUTAR:

COPY SYSTEM
│
├── 00 · VOICE
│
├── 01 · GLOSSARY
│
├── 02 · ACTIONS
│
├── 03 · STATES
│
├── 04 · FEEDBACK
│
├── 05 · NAVIGATION
│
├── 06 · AUTHORITY
│
├── 07 · OBJECTS
│
├── 08 · AREAS
│   ├── Workspace
│   ├── Projects
│   ├── Planning
│   ├── Execution
│   ├── Copilot
│   ├── Automations
│   ├── Reports
│   ├── Mapa-OS
│   └── Scanner
│
├── 09 · CHANNELS
│   ├── App
│   ├── Mobile
│   ├── Email
│   ├── WhatsApp
│   ├── Push
│   └── MCP
│
├── 10 · LOCALES
│
└── 11 · METRICS

Conclusão

Para o EXECUTAR, eu adotaria em 2026 a estratégia:

Copy Semantic System → Copy Tokens → Context Variants → Channel Adapters → Localization → Telemetry.

Não rota → escrever texto → próxima rota.

Seu CSV atual deve continuar existindo, mas como registro de aplicação da copy. Acima dele deve existir um Master Copy Registry, provavelmente com algo na faixa de 100–200 mensagens canônicas capazes de alimentar grande parte das 547 ocorrências atuais.

Isso reduz manutenção, melhora consistência App/Mobile/Copiloto/Scanner/Mapa-OS e cria uma estrutura adequada para geração assistida por IA sem perder governança semântica.