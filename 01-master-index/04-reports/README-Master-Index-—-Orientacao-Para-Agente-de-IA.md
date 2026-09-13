---
id: DOC-CLX-077
folder_id: FS-IDX-005
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "README Master Index — Orientacao Para Agente de IA"
sha256: 28ffa06fce699552244489302d9a9fef0a11408006f97b4a40e0c6374ca88b97
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

README Master Index — Orientacao Para Agente de IA

1. Identidade do pacote

|Campo           |Valor                                                         |
|----------------|--------------------------------------------------------------|
|ID              |WF-ORG-DIR-001                                                |
|VERSION         |1.0                                                           |
|AREA            |Multi-Agent SDK Blueprint / EXECUTAR                          |
|WORKFLOW        |Organizacao e verificacao de diretorio                        |
|OWNER           |A DEFINIR                                                     |
|STATUS          |VERIFIED                                                      |
|AUTOMATION_LEVEL|A4                                                            |
|HANDOFF         |Proximo agente deve reconciliar contratos e configurar runtime|

Este pacote e uma organizacao documental verificada do blueprint de um sistema multiagente. Ele nao deve ser tratado como SDK funcional pronto. A organizacao foi concluida, mas a configuracao integrada do runtime, dos agentes, das permissoes, dos handoffs e das ferramentas ainda depende das lacunas registradas em 00_GOVERNANCA/GAPS_E_CONFLITOS.md.

2. Estado verificado

|Evidencia                                                 |Resultado|
|----------------------------------------------------------|--------:|
|Arquivos de origem classificados                          |367      |
|Ocorrencias rastreadas, incluindo membros de ZIPs internos|706      |
|Areas principais                                          |16       |
|ZIPs internos unicos inspecionados                        |12       |
|Entradas `SKILL.md` catalogadas                           |17       |
|Nomes distintos de skills                                 |16       |
|Scripts locais candidatos                                 |15       |
|Schemas catalogados                                       |52       |
|Status da organizacao                                     |VERIFIED |
|Nivel de automacao                                        |A4       |

Validacoes registradas como PASS: CRC do ZIP externo, CRC dos ZIPs internos, cobertura de origem, preservacao por SHA-256, ausencia de colisoes de overwrite, sintaxe JSON/YAML gerada, paths de registros, preservacao de pacotes de skill, links Markdown locais previamente resolvidos e processamento da inbox.

3. Como iniciar

1. Abra 01_README_COMECE_AQUI.md para a leitura humana inicial.
2. Abra 00_MASTER_INDEX.md para navegar pelas 16 areas.
3. Consulte 00_GOVERNANCA/RELATORIO_ORGANIZACAO.md para o resumo do que foi feito.
4. Consulte 00_GOVERNANCA/RELATORIO_VALIDACAO.json para evidencias formais de verificacao.
5. Consulte 00_GOVERNANCA/GAPS_E_CONFLITOS.md antes de qualquer configuracao do SDK.
6. Use 00_MASTER_INDEX.json quando precisar de uma entrada por arquivo para automacao.
7. Para nova verificacao local, execute na raiz do pacote: python3 15_TESTS/verificar_pacote.py.

4. Principio de operacao para o proximo agente

O proximo agente deve operar por evidencia. Conteudo recebido de documentos, nomes de pastas, scaffolds, arquivos historicos e referencias preservadas nao deve ser promovido automaticamente para implementado, valido, instalado, disponivel ou publicado.

Regras obrigatorias:

|Regra                               |Aplicacao                                                                 |
|------------------------------------|--------------------------------------------------------------------------|
|Preservar IDs existentes            |Nao renomear IDs canonicos sem registrar origem, destino e justificativa  |
|Separar documento de implementacao  |Um PRD, schema ou scaffold nao prova runtime funcional                    |
|Nao preencher lacunas por inferencia|Campos sem fonte devem permanecer `A DEFINIR`                             |
|Resolver conflitos antes de integrar|Especialmente skills duplicadas e papeis de agentes                       |
|Manter rastreabilidade              |Toda alteracao deve apontar para fonte, decisao, evidencia e proximo passo|
|Verificar antes de declarar DONE    |DONE exige execucao, resultado esperado e evidencia                       |

5. Mapa das areas

|Area                     |Funcao                                                            |Uso pelo agente                                         |
|-------------------------|------------------------------------------------------------------|--------------------------------------------------------|
|`00_GOVERNANCA/`         |Identidade, inventario, proveniencia, relatorios, checksums e gaps|Fonte de controle e auditoria                           |
|`01_ORCHESTRATOR/`       |Orquestrador e pacote de roteamento cognitivo                     |Reconciliar papel central antes de runtime              |
|`02_AGENTS/`             |Scaffolds AGENT_001 a AGENT_003 e referencia VERA                 |Definir papeis, entradas, saidas e permissoes           |
|`03_HANDOFFS/`           |Contrato, schema e registro de handoffs                           |Validar passagem entre agentes                          |
|`04_SKILLS/`             |Bibliotecas de skills com estrutura interna preservada            |Escolher namespaces e resolver duplicidade              |
|`05_TOOLS/`              |Scripts e especificacoes de ferramentas                           |Verificar se cada tool e apenas candidata ou operacional|
|`06_CONTEXT/`            |Negocio, produto, arquitetura, design e Mapa-OS                   |Fonte de contexto documental                            |
|`07_MEMORY_STATE/`       |Contrato de estado e referencias de memoria                       |Definir persistencia e estado de execucao               |
|`08_POLICIES_GUARDRAILS/`|Politicas, permissoes e guardrails                                |Controlar autorizacoes e limites                        |
|`09_WORKFLOWS/`          |Workflows, metodologia e rotina do Copiloto                       |Selecionar proximo fluxo executavel                     |
|`10_OUTPUT_SCHEMAS/`     |Schemas e contratos de saida                                      |Validar outputs estruturados                            |
|`11_EVALS/`              |Gates, fixtures e avaliacoes                                      |Preparar validacao funcional                            |
|`12_OBSERVABILITY/`      |Scaffold de tracing                                               |Definir logs, rastros e observabilidade                 |
|`13_RUNTIME_CONFIG/`     |Runtime e variaveis de ambiente                                   |Completar configuracao pendente                         |
|`14_DEPLOYMENT/`         |Scaffold de implantacao                                           |Preparar release somente apos runtime verificado        |
|`15_TESTS/`              |Plano e script de verificacao do pacote                           |Rodar integridade documental                            |
|`99_INBOX_ARRASTE_AQUI/` |Entrada futura de materiais                                       |Classificar novos arquivos antes de integrar            |

6. Registros principais

|Arquivo                                   |Finalidade                                           |
|------------------------------------------|-----------------------------------------------------|
|`00_MASTER_INDEX.md`                      |Navegacao executiva pelas areas                      |
|`00_MASTER_INDEX.json`                    |Indice completo por arquivo para leitura automatica  |
|`00_GOVERNANCA/MANIFESTO_ORGANIZACAO.json`|Origem, destino e hash dos arquivos recebidos        |
|`00_GOVERNANCA/MAPA_ORIGEM_DESTINO.csv`   |Mapa tabular de movimentacoes e consolidacoes        |
|`00_GOVERNANCA/CHECKSUMS.json`            |Evidencia de integridade                             |
|`00_GOVERNANCA/RELATORIO_VALIDACAO.json`  |Resultado formal dos checks                          |
|`00_GOVERNANCA/GAPS_E_CONFLITOS.md`       |Bloqueios, lacunas e conflitos do proximo workflow   |
|`00_GOVERNANCA/DUPLICIDADES.json`         |Grupos com conteudo SHA-256 identico                 |
|`00_GOVERNANCA/CONTRATO_WORKFLOW.yaml`    |Escopo, controle e criterios de aceite da organizacao|
|`04_SKILLS/skill_registry.yaml`           |Skills efetivamente presentes no pacote              |
|`05_TOOLS/tool_registry.yaml`             |Scripts locais candidatos                            |
|`10_OUTPUT_SCHEMAS/schema_registry.yaml`  |Schemas com paths canonicos locais                   |

7. Lacunas que bloqueiam a configuracao funcional

|ID              |Status          |Descricao                                                                                                                  |Impacto                                                              |
|----------------|----------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|GAP-ORG-001     |A DEFINIR       |Scaffolds de runtime e agentes tem campos vazios; nao ha mapeamento comprovado entre AGENT_001/002/003 e papeis documentais|Bloqueia configuracao integrada do SDK                               |
|CONFLITO-ORG-001|NEEDS_RESOLUTION|Existem duas distribuicoes com o nome `executar-status-report`                                                             |Bloqueia roteamento automatico apenas por nome                       |
|GAP-ORG-002     |BLOCKED         |Catalogo MCP citado por documentos nao esta incluido no ZIP                                                                |Bloqueia cadastro completo das tools MCP                             |
|GAP-ORG-003     |A DEFINIR       |Router cita 99 skills, mas este pacote contem 17 `SKILL.md` e 16 nomes distintos                                           |Bloqueia afirmacao de disponibilidade das 99 skills                  |
|GAP-ORG-004     |DOCUMENTED      |Links sandbox historicos foram preservados, mas nao sao evidencia de acesso atual                                          |Exige uso dos indices locais ou recuperacao externa quando necessaria|

8. Workflow recomendado para o proximo agente

|Ordem|No executavel             |Entrada                                                          |Saida esperada                                        |Verificacao                                           |
|----:|--------------------------|-----------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|1    |Reconciliar agentes       |`02_AGENTS/`, `01_ORCHESTRATOR/`, `03_AGENT_GRAPH.yaml`          |Mapa AGENT_ID -> papel -> input -> output -> permissao|Campos sem evidencia ficam `A DEFINIR`                |
|2    |Resolver skills duplicadas|`04_SKILLS/skill_registry.yaml`, pacotes preservados             |Namespace e pacote canonico para cada skill           |Conflito `executar-status-report` resolvido ou isolado|
|3    |Reconciliar tools MCP     |`05_TOOLS/`, gaps, documentos externos recuperados se disponiveis|Tool catalog verificavel                              |Nenhuma capability promovida sem fonte                |
|4    |Configurar runtime        |`13_RUNTIME_CONFIG/`, `08_POLICIES_GUARDRAILS/`                  |Runtime minimo documentado                            |Variaveis e permissoes explicitadas                   |
|5    |Validar handoffs          |`03_HANDOFFS/`, `10_OUTPUT_SCHEMAS/`                             |Fluxos de passagem testaveis                          |Schema valida payloads de teste                       |
|6    |Preparar evals            |`11_EVALS/`, `15_TESTS/`                                         |Gate funcional do SDK                                 |Resultado registrado em relatorio novo                |

9. Criterios de aceite para continuidade

O proximo workflow so deve ser marcado como DONE quando:

|Criterio       |Exigencia                                                              |
|---------------|-----------------------------------------------------------------------|
|Completude     |Todas as entradas requeridas foram lidas ou registradas como ausentes  |
|Consistencia   |IDs, nomes e paths nao entram em conflito                              |
|Rastreabilidade|Cada decisao aponta para arquivo, trecho, evidencia ou lacuna          |
|Execucao       |A acao prevista foi realmente executada quando autorizada              |
|Verificacao    |Houve teste, validacao de schema, hash, log ou outra evidencia objetiva|
|Registro       |O novo estado foi salvo em relatorio, indice ou checkpoint             |

10. Entrega e handoff

Estado atual: VERIFIED para organizacao documental.
Estado do SDK: configuracao funcional pendente.
Proximo workflow preparado: reconciliacao e configuracao dos contratos do SDK.

O agente sucessor deve iniciar por 00_GOVERNANCA/GAPS_E_CONFLITOS.md, depois cruzar 00_MASTER_INDEX.json com os registros de skills, tools, schemas, runtime e handoffs. Qualquer decisao nova deve atualizar os registros de governanca antes de alterar runtime, deploy ou automacao.