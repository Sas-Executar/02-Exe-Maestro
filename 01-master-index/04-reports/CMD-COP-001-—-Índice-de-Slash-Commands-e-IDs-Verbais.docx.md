---
id: DOC-CLX-075
folder_id: FS-IDX-005
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "CMD-COP-001 — Índice de Slash Commands e IDs Verbais.docx"
sha256: 0e8d43dad74cb212f1bc10462b02becd53bbabab7af230b6c2fead635cd8846e
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

CMD-COP-001 — ÍNDICE DE COMANDOS E IDS VERBAIS

REGRA

O usuário pode operar por comando com barra ou por frase equivalente. O Orquestrador resolve o ID verbal e carrega somente o módulo necessário.

COMANDOS DE ROTINA

CV-BOMDIA-001 — /bomdia — abrir o dia, validar continuidade e mostrar trabalho liberado.

CV-AGORA-001 — /agora — mostrar somente o objeto atual, duração, DoD, evidência e próxima ação.

CV-ESTADO-001 — /estado — mostrar progresso, Sprint/C72, Gate, bloqueios e estado atual.

CV-FECHAR-001 — /fechardia — validar resultado, evidência, registrar transição e preparar continuidade.

CV-REPLAN-001 — /replanejamento — recalcular apenas o trecho afetado por dependências, capacidade ou bloqueio.

CV-MAPA-001 — /mapa — emitir MAPA-OS visual a partir da fonte canônica.

CV-EVID-001 — /evidencia — consultar ou registrar evidência do objeto atual.

CV-BLOQ-001 — /bloqueio — registrar impedimento ou consultar bloqueios ativos.

COMANDOS DE PRODUTIVIDADE

CV-ATUAL-001 — /atualizar — sincronização mínima de tarefas e contexto.

CV-ATUAL-002 — /atualizar-abrangente — varredura profunda somente quando necessária.

CV-CONTEXTO-001 — /contexto — recuperar contexto necessário ao objeto atual.

CV-MEMORIA-001 — /memoria — consultar ou ajustar memória operacional.

COMANDOS DE OPERAÇÕES

CV-CAP-001 — /capacidade — planejar ou validar capacidade.

CV-MUD-001 — /mudanca — estruturar mudança que afete escopo, processo ou sistema.

CV-PROC-001 — /processo — documentar processo.

CV-POP-001 — /procedimento — criar ou consultar procedimento operacional.

CV-SIT-001 — /situacao — emitir situação operacional compacta.

CV-FORN-001 — /fornecedor — avaliar fornecedor.

CV-RISCO-001 — /risco — avaliar risco do objeto atual.

CV-CONF-001 — /conformidade — validar critérios, normas e evidências.

CV-OTIM-001 — /otimizar — reduzir desperdício, duplicação, espera e fricção do fluxo atual.

SINÔNIMOS VERBAIS

“Bom dia, copiloto” = /bomdia.

“O que faço agora?” = /agora.

“Como estamos?” = /estado.

“Terminei por hoje” = /fechardia.

“Preciso mudar o plano” = /replanejamento.

“Me mostra o mapa” = /mapa.

“Estou bloqueado” = /bloqueio.

REGRAS DE INTERAÇÃO

- Um comando deve produzir uma ação principal, não um relatório geral.

- O usuário não precisa informar o módulo.

- O usuário não precisa repetir IDs conhecidos quando o contexto atual for inequívoco.

- Se houver ambiguidade material entre dois objetos, o Orquestrador pede a mínima decisão necessária.

- Comandos antigos do legado podem ser aceitos como aliases, mas a interface preferida usa os comandos curtos deste índice.

- Todas as respostas visíveis em português do Brasil.

MAPEAMENTO DO LEGADO DE OPERAÇÕES

/planejar-capacidade → /capacidade.

/solicitar-mudanca → /mudanca.

/documentar-processo → /processo.

/procedimento-operacional → /procedimento.

/relatorio-situacao → /situacao.

/avaliar-fornecedor → /fornecedor.

CRITÉRIO DE ACEITE

O operador deve conseguir conduzir o dia apenas com /bomdia, /agora, /estado, /fechardia e /replanejamento; os demais comandos são disclosure progressivo para situações específicas.