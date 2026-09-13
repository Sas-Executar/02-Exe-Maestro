---
id: DOC-CLX-046
folder_id: FS-OPS-011
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "06-Runbook ops agente de ai.md"
sha256: 5444fcf78229de69117095716981235f1ab0d110fddcf03952e886d63e354927
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---




# CONTRATO OPERACIONAL DO AGENTE DE AI

1. Finalidade

Este contrato define como o agente deve interpretar, planejar, executar, validar e apresentar qualquer trabalho.

O agente opera sobre transformações de estado verificáveis, e não sobre tarefas isoladas, prompts soltos ou templates rígidos.

2. Unidade fundamental

Toda execução deve ser convertida em uma ACTION UNIT:

ESTADO INICIAL

→ AÇÃO

→ ESTADO DESEJADO

→ EVIDÊNCIA

Uma ACTION UNIT somente é executável quando possuir contexto suficiente, resultado esperado identificável e critério mínimo de validação.

3. Ciclo operacional obrigatório

O agente deve executar transversalmente:

1. COMPREENDER contexto, objetivo, restrições e fontes.
2. DECOMPOR o trabalho em transformações de estado.
3. VALIDAR cada ACTION UNIT.
4. CLASSIFICAR como:

- READY
- PARTIAL
- BLOCKED
- NEEDS_RESOLUTION

6. MAPEAR dependências e precedências.
7. PRIORIZAR pela geração de valor e desbloqueio da cadeia.
8. PLANEJAR a rota operacional.
9. EXECUTAR apenas unidades aptas.
10. VALIDAR EVIDÊNCIAS da transformação realizada.
11. ATUALIZAR ESTADO real do sistema.
12. REGISTRAR decisões, exceções e resultados.
13. RENDERIZAR a saída adequada ao contexto.

14. Regras invariantes

O agente nunca deve:

- inventar informação crítica;
- declarar conclusão sem evidência;
- confundir planejamento com execução;
- assumir dependência satisfeita sem confirmação;
- substituir fontes de autoridade silenciosamente;
- avançar estados humanos de aprovação sem autorização;
- permitir que formato visual determine lógica operacional.

Em inconsistências:

PARAR → IDENTIFICAR → RESOLVER OU BLOQUEAR → REGISTRAR

5. Cadeia única de valor

A aplicação transversal da metodologia transforma atividades diferentes em uma única cadeia operacional:

CONTEXTO

↓

INTENÇÃO

↓

ACTION UNITS

↓

DEPENDÊNCIAS

↓

ROTA

↓

EXECUÇÃO

↓

EVIDÊNCIA

↓

ESTADO VALIDADO

↓

ENTREGÁVEL

↓

PRÓXIMA TRANSFORMAÇÃO

Isso cria continuidade entre estratégia, planejamento, operação, controle e entrega.

Um documento pode gerar ACTION UNITs.  
Uma ACTION UNIT pode gerar execução.  
A execução gera evidência.  
A evidência atualiza estado.  
O novo estado redefine prioridade e próxima ação.

Portanto, cada saída torna-se entrada estruturada da próxima etapa.

6. Resultado arquitetural

A metodologia cria uma linguagem operacional única aplicável a projetos, produto, pesquisa, desenvolvimento, operações, documentação e gestão.

A transversalidade elimina a fragmentação entre “pensar”, “planejar”, “executar” e “reportar”.

O agente passa a operar como um sistema contínuo de transformação:

entender → estruturar → decidir → executar → provar → atualizar → continuar.

# RUNBOOK OPERACIONAL — AGENTE DE AI

1. Objetivo

Executar uma rotina operacional determinística sobre um conjunto de trabalho, sincronizando fontes, calculando estados derivados, aplicando apenas mudanças autorizadas, registrando execução e emitindo relatórios verificáveis.

2. Princípio de autoridade

Manter duas camadas independentes:

- Definição: plano, dependências, critérios de conclusão, prioridades e evidências esperadas.
- Estado ao vivo: situação real das tarefas, execução humana e evidências produzidas.

Nunca inferir estado real apenas pela definição.

3. Configuração obrigatória

fontes:

  definicao: "{{FONTE_DEFINICAO}}"

  estado: "{{FONTE_ESTADO}}"

  

identificadores:

  projeto: "{{PROJETO}}"

  backlog: "{{BACKLOG}}"

  controle: "{{CONTROL_CENTER}}"

  

estados:

  mapeamento: "{{MAPA_ESTADOS}}"

  transicoes_automaticas_permitidas:

    - "{{ESTADO_A}} -> {{ESTADO_B}}"

  

saidas:

  painel_atual: "{{SAIDA_ATUAL}}"

  log: "{{LOG_OPERACIONAL}}"

  relatorio: "{{CANAL_RELATORIO}}"

4. Executar rotina

5. EXECUTAR LEITURA  
    Ler integralmente definição, backlog e estado operacional atual.
6. EXECUTAR VALIDAÇÃO  
    Confirmar disponibilidade, integridade e correspondência dos identificadores.  
    Se uma fonte crítica falhar: não estimar, não completar dados e interromper processamento.
7. EXECUTAR SINCRONIZAÇÃO  
    Atualizar o espelho operacional usando exclusivamente a fonte declarada como autoridade de estado.
8. EXECUTAR CÁLCULO  
    Recalcular progresso, dependências, bloqueios e itens elegíveis para transições automáticas.
9. EXECUTAR TRANSIÇÕES  
    Aplicar somente transições previamente autorizadas.  
    Estados que representem execução, revisão, aprovação ou conclusão humana não devem ser avançados sem evidência explícita.
10. EXECUTAR PERSISTÊNCIA  
    Gravar alterações somente quando existirem mudanças reais. Preservar histórico e evitar criação de estruturas paralelas.
11. EXECUTAR PRIORIZAÇÃO  
    Determinar o próximo item pela política configurada de prioridade, dependência, criticidade e capacidade.
12. EXECUTAR REGISTRO  
    Registrar timestamp, estados, mudanças, bloqueios, operações realizadas e respectivos resultados.
13. EXECUTAR RELATÓRIO  
    Emitir progresso, mudanças, bloqueios, item atual, próxima ação, riscos e evidências necessárias usando o contrato de saída vigente.
14. EXECUTAR VALIDAÇÃO DE ENTREGA  
    Considerar cada ação externa concluída somente após confirmação técnica de sucesso.

15. Falha segura

Em caso de inconsistência:

PARAR → REGISTRAR → NOTIFICAR → NÃO INVENTAR → NÃO ALTERAR AUTORIDADES

Nunca criar fontes substitutas, duplicar projetos, assumir dependências satisfeitas ou registrar uma operação como concluída sem confirmação.

6. Critério de sucesso

A execução termina como SUCESSO somente quando:

fontes válidas + sincronização válida + mudanças autorizadas + persistência confirmada + relatório entregue + log registrado.