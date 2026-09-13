---
id: DOC-CLX-039
folder_id: FS-EXE-001
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "PRD-001_EXECUTAR_GESTAO_MULTICANAL_STANDALONE.md"
sha256: f7a0c79177dc89c5ee3e74df8250dbbfcc0946462a5cbb6ded39a2311a7a95ae
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# PRD — EXECUTAR · Gestão Multicanal Standalone

## 1. Visão do Produto

O EXECUTAR deve permitir que um usuário gerencie projetos, tarefas, entregáveis, prazos, evidências e decisões sem depender de uma interface específica.

O aplicativo completo existe como uma das superfícies possíveis de gestão, mas não deve ser obrigatório para a operação cotidiana.

**Princípio central:** o projeto é único; a interface de execução é substituível.

O usuário deve poder escolher operar integralmente por qualquer uma das seguintes superfícies:

1. Aplicativo
2. Papel + Scanner
3. Canal de comunicação
4. Agente de IA

Cada superfície deve funcionar de maneira standalone, mantendo acesso ao mesmo estado operacional do projeto.

## 2. Problema

Ferramentas tradicionais de gestão obrigam o usuário a retornar constantemente ao aplicativo para consultar tarefas, alterar status, registrar progresso, reagendar, adicionar evidências, verificar prazos, criar novos itens, consultar contexto e decidir o próximo passo.

No EXECUTAR, o centro deve ser o objeto de execução, e não o aplicativo.

## 3. Hipótese de Produto

Se todas as interfaces operarem sobre o mesmo modelo de execução e possuírem capacidade suficiente para consultar e alterar seu estado, o usuário poderá administrar seu trabalho pelo meio mais adequado ao contexto sem perder continuidade.

Exemplo de continuidade:
- segunda-feira: imprime o planejamento semanal;
- terça-feira: atualiza tarefas exclusivamente escaneando o papel;
- quarta-feira: responde por e-mail solicitando reagendamento;
- quinta-feira: conversa com o agente de IA e reorganiza prioridades;
- sexta-feira: abre o aplicativo e encontra todo o estado consolidado.

Nenhuma dessas transições deve exigir reconstrução de contexto.

## 4. Princípio Arquitetural

Todas as superfícies devem ler e escrever sobre o mesmo **Execution State**.

Não existem “tarefas do scanner”, “tarefas do WhatsApp”, “tarefas do aplicativo” ou “tarefas do agente”.

Existe somente o mesmo objeto de execução, representado de forma diferente conforme o canal.

## 5. Modo A — Aplicativo

O aplicativo oferece a interface visual completa e permite criar projetos, estruturar entregáveis, criar tarefas, definir prazos, consultar calendário, revisar contexto, anexar evidências, reagendar, priorizar, revisar histórico, executar check-in/check-out e gerar materiais impressos.

É a superfície com maior densidade informacional, mas não constitui requisito para utilização das demais.

## 6. Modo B — Papel + Scanner

O usuário pode imprimir representações físicas do seu sistema de execução, incluindo prisma, tripé/tríptico, A4, planejamento semanal, roadmap, calendário, ficha de entregável e ficha de tarefa.

O papel deve funcionar como uma interface física do sistema, não apenas como relatório estático.

Ao apontar a câmera para o material, o scanner deve reconhecer documento, projeto, entregável, período, tarefas e elementos interativos associados.

O scanner adiciona controles contextuais para concluir, reagendar, bloquear, anexar evidência, acessar detalhes ou executar outras ações permitidas.

**Objetivo:** permitir uma semana de trabalho sem abrir a interface principal do aplicativo.

## 7. Modo C — Comunicação

O usuário pode escolher um canal conversacional para administrar o sistema, como e-mail, chat interno, WhatsApp ou integrações futuras.

A interação pode ocorrer por linguagem natural ou ações estruturadas.

O sistema interpreta a intenção do usuário, confirma quando necessário e atualiza o estado do projeto.

A comunicação deixa de ser apenas notificação e passa a funcionar como interface operacional.

## 8. Modo D — Agente de IA

O agente constitui a camada de maior autonomia.

O usuário pode delegar objetivos, e o agente pode analisar tarefas, prioridades, capacidade, calendário, dependências, histórico, prazos, evidências e bloqueios.

Dentro de limites de autoridade definidos, o agente pode reorganizar tarefas, sugerir prioridades, reagendar, criar subtarefas, detectar riscos, solicitar informações, preparar check-ins, cobrar pendências, registrar atualizações e gerar novos materiais de execução.

## 9. Standalone como Requisito Fundamental

Cada superfície deve possuir autonomia operacional suficiente para que o usuário não seja forçado a migrar para outra interface durante uma rotina normal.

Standalone não significa sistemas separados; significa interfaces independentes operando sobre um único sistema.

## 10. Continuidade entre Superfícies

Uma alteração realizada em qualquer superfície deve aparecer imediatamente nas demais.

Exemplo:
1. usuário conclui uma tarefa pelo scanner;
2. estado central é atualizado;
3. planejamento é recalculado;
4. agente recebe o novo contexto;
5. próximo e-mail considera a tarefa concluída;
6. aplicação apresenta a mesma informação.

## 11. Objeto Central

A arquitetura deve ser organizada prioritariamente pelo **Objeto de Execução**, que pode conter:
- objetivo;
- status;
- prazo;
- tarefas;
- dependências;
- agenda;
- contexto;
- evidências;
- decisões;
- histórico;
- próximo passo.

Cada interface decide apenas como representar e manipular esse objeto.

## 12. Separação entre Estado e Representação

O estado deve ser independente da superfície.

Exemplo de um mesmo estado:
- deadline;
- status;
- progresso;
- próxima ação;
- risco.

Esse mesmo estado pode ser representado no app, papel, e-mail, WhatsApp, chat ou agente.

## 13. Scanner como Bridge Físico-Digital

O scanner deve ser tratado como interface de primeira classe.

Fluxo:
**Físico → Identificação → Contexto Digital → Ação → Automação → Estado Atualizado**

O papel fornece contexto espacial e cognitivo; o scanner adiciona capacidade computacional.

## 14. Papel como Interface Persistente

O material físico pode permanecer sobre a mesa, junto ao computador, na parede, dentro do caderno ou montado em formato prisma.

O usuário mantém uma representação persistente do trabalho sem permanecer conectado ao aplicativo.

O scanner é utilizado quando uma interação digital é necessária.

## 15. Interaction Contract

As ações fundamentais devem existir independentemente da superfície:

- CREATE
- VIEW
- UPDATE
- COMPLETE
- DEFER
- REPLAN
- BLOCK
- ATTACH
- COMMENT
- DELEGATE
- CANCEL

Cada canal implementa esses verbos de forma apropriada à sua interface.

## 16. Princípio UX

O usuário não escolhe qual sistema utilizar; escolhe como quer interagir com o mesmo sistema naquele momento.

A superfície pode mudar continuamente, enquanto o estado permanece único.

## 17. Níveis de Autonomia

- **Nível 1 — Manual:** usuário executa diretamente no aplicativo.
- **Nível 2 — Assistido:** usuário opera por scanner ou mensagens.
- **Nível 3 — Conversacional:** usuário expressa intenções e o sistema traduz em operações.
- **Nível 4 — Delegado:** usuário fornece objetivos e limites, e o agente administra a execução dentro dessas restrições.

## 18. Guardrails

A autonomia não pode eliminar o controle do usuário.

Operações devem possuir níveis de autoridade:
- somente leitura;
- ações reversíveis;
- alterações operacionais;
- replanejamento;
- ações externas/críticas.

Operações sensíveis devem exigir aprovação conforme política definida pelo usuário.

## 19. Auditabilidade

Toda mudança deve registrar:
- WHAT — ação realizada;
- WHEN — momento;
- WHO — usuário ou agente;
- WHERE — app, scanner, e-mail, WhatsApp, chat ou agente;
- WHY — comando, regra ou contexto que originou a alteração.

## 20. Critério de Sucesso Principal

O produto atinge sua proposta quando um usuário consegue passar uma semana inteira administrando um projeto pelo papel e scanner, sem abrir a interface principal do EXECUTAR, e ao retornar ao aplicativo encontra o projeto completamente atualizado e consistente.

O mesmo critério deve ser válido individualmente para comunicação e agente de IA.

## 21. North Star

Métrica principal sugerida: **Executed Objects Without UI Dependency**.

Indicadores complementares:
- % de ações executadas fora da UI principal;
- % de semanas executadas multicanal;
- % de operações concluídas via scanner;
- % de operações conversacionais;
- % de ações delegadas ao agente;
- consistência de estado entre canais;
- sessões standalone concluídas;
- tempo para atualização do estado de execução.

## 22. Proposta Central

O EXECUTAR deve ser tratado como um **Execution System com interfaces substituíveis**.

O software existe como estado, regras, contexto, automações e inteligência.

App, papel, scanner, e-mail, WhatsApp, chat e agente são superfícies pelas quais o usuário acessa e modifica o mesmo sistema.

**Diferencial:** não apenas permitir várias interfaces, mas garantir que qualquer uma delas possa ser suficiente.
