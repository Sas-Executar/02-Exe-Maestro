---
id: DOC-CLX-036
folder_id: FS-OPS-010
tipo: documento-importado
status: referência
origem: export-claude-20260913
origem_filename: "✅ PMI X TDHA X Evidencias - 21.08.docx"
sha256: c22884bd8f77ddf7215df789db38fb6e1996eeece8a2ee2644ac51020a1e78c8
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

[Pesquisa] · DATA-ADHD-PM-001

DOCUMENT READER · VALU-MODE V3

⸻

ID DATA-ADHD-PM-001
Tipo Pesquisa · Matriz de evidências e implicações de produto
Owner Não determinado
Versão 1.0
Data 19/08/2026
Fase Síntese e correlação
Projeto Não determinado
PARA Produto · Arquitetura neuroinclusiva baseada em evidências
Referência JSON AEVO · HOJE > Preencher(1).md · PMBOK® Guide 8 · NIMH · NICE · literatura científica
3# #TDAH #gestaodeprojetos #neurodesign

⸻

## **RESUMO EXECUTIVO**

O quê Matriz paralela Gestão de Projetos → exigência humana → vulnerabilidade associada ao TDAH → impacto operacional → compensação sistêmica → decisão de produto.
Por quê Testar a tese de que parte da carga normalmente deixada para o usuário pode ser deslocada para arquitetura, regras e automação do sistema.
Quem Adultos com TDAH executando trabalho intelectual/projetos; produto, design e engenharia que constroem o sistema.
Como Funções de projeto extraídas do documento-base e confrontadas com PMI, NIMH/NICE e estudos sobre funções executivas em TDAH adulto.

⸻

## **3P+N · APLICAÇÃO**

Problema A gestão de projetos pressupõe diversas operações cognitivas — planejar, organizar, priorizar, lembrar, acompanhar, estimar tempo, iniciar e concluir — justamente em domínios nos quais adultos com TDAH **podem**, com grande heterogeneidade individual, apresentar dificuldades.
Processo Decompor cada função operacional e procurar correspondência clínica e neuropsicológica, evitando transformar associação em causalidade universal.
Progresso A hipótese central é **parcialmente sustentada**: há convergência forte para organização, planejamento, gestão temporal, atenção sustentada e conclusão; evidência moderada para memória prospectiva, flexibilidade e metacognição.
Next 01 Transformar a matriz abaixo em requisitos funcionais e princípios de design verificáveis.
Next 02 Separar evidência clínica de decisão de arquitetura, mantendo cada feature como hipótese testável.

[Operação] · DRIVE-PROD-002

DOCUMENT READER · VALU-MODE V3

⸻

ID DRIVE-PROD-002
Tipo Operação · Registro de schema CSV
Owner Não determinado
Versão 1.0
Data 19/08/2026
Fase Registrado · verificado
Projeto Não determinado
PARA Produto · Pesquisa e estruturação progressiva
Referência Tag Produto · DATA-ADHD-PM-001
3# #schema #produto #evidencia

⸻

## **RESUMO EXECUTIVO**

O quê Schema da matriz Gestão de Projetos × TDAH registrado em CSV.
Por quê Preservar a estrutura antes da expansão da pesquisa, sem antecipar conteúdo de PRD, FRD, persona ou jornadas.
Quem Produto · Pesquisa · Design · Engenharia.
Como CSV contendo apenas cabeçalhos estruturais e campos de governança; nenhuma linha de conteúdo preenchida.

⸻

## **3P+N · APLICAÇÃO**

Problema A matriz ainda precisa ser expandida antes de alimentar os tópicos de Produto.
Processo Formalização do contrato tabular → exportação CSV → registro na raiz de Tag Produto → verificação.
Progresso **Concluído e verificado.** O CSV está na pasta correta.
Next 01 Expandir e validar o schema/evidências antes de distribuir conteúdo entre 2.2–2.12.

## **Registro criado**

**SCHEMA_MATRIZ_GESTAO_TDAH_V1.csv**

Local:

Tag Produto / SCHEMA_MATRIZ_GESTAO_TDAH_V1.csv

A pasta Tag Produto utilizada é a pasta já existente no Drive.

O diretório foi verificado após a operação: o CSV aparece na raiz ao lado das subpastas **2.2 a 2.12**, sem criação de documentos dentro desses tópicos.

### **Schema registrado**

schema_version

row_id

funcoes_fundamentais_gestao_projetos

funcoes_executivas_area_gestao_projetos

capacidades_humanas_operacionais_exigidas

funcao_deficit_tdah

fonte_clinica

fonte_cientifica

funcao_executiva_cognitiva

evidencia

impacto_operacional_funcao_afetada

impacto_operacional_mecanismo

impacto_operacional_consequencia

impacto_operacional_compensacao

conclusao_produto_design

classe_epistemica

estado_validacao

observacoes

**Estado epistemológico:** o arquivo contém **estrutura**, não evidência consolidada.
**Estado documental:** existente + registrado + verificado; **não preenchido, não aprovado como schema final e não distribuído nos tópicos de Produto**.

[**Abrir o CSV no Google Drive**](https://drive.google.com/file/d/1wweF34-T27l7Jmikw_CCcfL1-PylvH2y/view?usp=drivesdk)

# **1. ACHADO CENTRAL**

Seu documento-base formula exatamente a hipótese a ser testada: se priorização, iniciação, memória de trabalho, controle temporal, planejamento de longo prazo, troca de contexto e percepção da própria capacidade criarem atrito, o sistema deveria absorver parte dessas operações.

A literatura permite sustentar boa parte dessa direção, **mas não permite declarar que toda pessoa com TDAH possui todos esses déficits**. O NIMH descreve em adultos dificuldades possíveis com organização, procrastinação, planejamento, gestão de tempo, lembrança de tarefas, manutenção de foco e conclusão de grandes projetos. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) Meta-análises encontram diferenças de função executiva entre grupos com e sem TDAH, mas também mostram heterogeneidade substancial; portanto, TDAH ≠ déficit executivo global obrigatório. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/16116936/?utm_source=chatgpt.com))

Do lado da gestão de projetos, seu JSON já estrutura iniciação/escopo → planejamento → execução → monitoramento/finalização. Isso é compatível com a organização tradicional dos processos de gestão e, na edição atual, o PMBOK® Guide 8 também enfatiza domínios como governança, escopo, cronograma, stakeholders, recursos e risco. ([Project Management Institute](https://www.pmi.org/standards/pmbok))

# **2. MATRIZ TABULAR PRINCIPAL**

| **ID** | **Funções fundamentais de gestão de projetos** | **Funções executivas de uma área de gestão de projetos** | **Capacidades humanas / operacionais exigidas** | **FUNÇÃO / DÉFICIT TDAH associado** | **Fonte clínica** | **Fonte científica** | **Função executiva** | **Evidência** | **IMPACTO · função afetada** | **Mecanismo → consequência** | **Compensação sistêmica** | **CONCLUSÃO DE PRODUTO / DESIGN** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **GP-01** | **Iniciação e escopo**: necessidades, riscos, restrições, viabilidade | Definir problema, objetivo, limites e critérios | Manter múltiplas variáveis; abstrair estado futuro; decidir | Organização/planejamento podem ser frágeis; grandes tarefas podem gerar procrastinação | NIMH relata desorganização, planejamento deficiente e dificuldade com grandes projetos. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Meta-análise em TDAH adulto encontra diferenças moderadas em medidas executivas. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/16116936/?utm_source=chatgpt.com)) | Planejamento · memória de trabalho · controle executivo | **C · moderada/forte** | Definição do projeto | Muitas decisões simultâneas → sobrecarga → escopo incompleto ou início postergado | Brief guiado; progressive disclosure; restrições externalizadas; uma decisão por etapa | **O sistema deve estruturar o projeto antes de pedir ao usuário que o gerencie. E · Inferido** |
| **GP-02** | **Planejamento**: plano de ação, responsáveis, prazos, cronograma | Converter objetivo em trabalho executável | Sequenciar, decompor, organizar, prever dependências | Dificuldades de planejamento/organização | NIMH inclui má gestão de tempo, planejamento e organização entre dificuldades funcionais possíveis. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Boonstra et al.; Pievsky & McGrath sintetizam alterações neurocognitivas/executivas em TDAH. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/16116936/?utm_source=chatgpt.com)) | Planejamento · working memory · organização | **C · forte para associação; não universal** | Formação do plano | Objetivo macro exige muitas transformações mentais → plano incompleto ou pouco executável | **Projeto → entregável → tarefa → ação atômica**, dependências calculadas | **Decomposição deve ser função do motor, não trabalho cognitivo repetido do usuário. E** |
| **GP-03** | **Priorizar e sequenciar** | Garantir aderência a metas; determinar ordem de ação | Comparar valor, urgência, dependências e custo | Priorização/organização podem ser prejudicadas; não é um critério diagnóstico isolado | Revisões clínicas descrevem dificuldade de auto-organização, priorização e início; NIMH recomenda trabalhar organização e tarefas sensíveis ao tempo. ([PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2957278/?utm_source=chatgpt.com)) | Modelos de EF em TDAH associam comportamento dirigido a metas à autorregulação executiva. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/20667287/?utm_source=chatgpt.com)) | Goal management · inibição · planejamento | **C · moderada** | Escolha do próximo trabalho | Reavaliar continuamente alternativas → custo decisório → seleção instável/adiamento | Motor de prioridade usando dependência, critical path, prazo, bloqueio e valor + override humano | **Não oferecer apenas uma lista: oferecer “próxima ação recomendada + por quê”. E** |
| **GP-04** | **Cronograma e prazos** | Apoiar cumprimento de prazos e sincronizar atividades | Estimar duração; perceber passagem do tempo; lembrar eventos futuros | Má gestão de tempo é clinicamente descrita; percepção temporal mostra resultados heterogêneos | NIMH cita explicitamente gestão de tempo deficiente e dificuldade com compromissos. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Revisão de percepção temporal em adultos conclui que há evidência relevante, mas não sustenta um déficit temporal universal. ([PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9962130/?utm_source=chatgpt.com)) | Organização temporal · memória prospectiva | **C · moderada / heterogênea** | Schedule | Dependência de estimativa intuitiva → atraso, compressão do prazo, planejamento otimista | Tempo externalizado; marcos visíveis; buffers; dados históricos; previsão probabilística | **Tempo deve ser observado pelo sistema, não presumido pelo usuário. E** |
| **GP-05** | **Iniciar execução** | Colocar o plano em movimento | Transição intenção → ação; selecionar primeiro comportamento; reduzir ambiguidade | Procrastinação e dificuldade de iniciar tarefas aparecem clinicamente | NIMH registra procrastinação; literatura clínica adulta descreve dificuldade de começar tarefas. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Estudos de memória prospectiva mostram que adultos com TDAH podem ter dificuldade para planejar e executar intenções futuras. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/23484020/?utm_source=chatgpt.com)) | Ativação dirigida a objetivo · planejamento prospectivo | **C · moderada** | Start | Tarefa abstrata/grande → alto custo de ativação → não iniciar | Mostrar somente primeira ação concreta; critérios de conclusão explícitos; botão iniciar imediato | **A unidade de interface deve começar executável, não apenas informativa. E** |
| **GP-06** | **Execução** | Produzir entregas conforme plano e prazo | Atenção sustentada; persistência; inibição de distrações; memória operacional | Distratibilidade, dificuldade em manter-se na tarefa e terminar projetos | NIMH: dificuldade de atenção, distração, manutenção da tarefa e conclusão. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Estudos experimentais em adultos encontram prejuízo em atenção sustentada e deterioração relacionada ao tempo-na-tarefa. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/26206605/?utm_source=chatgpt.com)) | Atenção sustentada · inibição | **B/C · forte** | Trabalho em andamento | Competição entre estímulos + duração → abandono, fragmentação ou múltiplos trabalhos parcialmente abertos | **Modo foco**, WIP baixo, fila separada, captura de interrupções sem abandonar tarefa atual | **1 ação dominante + queue secundária é uma arquitetura coerente com a evidência. E** |
| **GP-07** | **Monitorar execução e progresso** | Acompanhar status, entregas, prazo e indicadores | Lembrar intenções; comparar estado atual × objetivo; autocontrole | Esquecimento de tarefas + dificuldades de memória prospectiva | NIMH cita dificuldade em lembrar tarefas diárias. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Fuermaier et al. observaram comprometimento em memória prospectiva complexa, especialmente ligado ao planejamento. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/23484020/?utm_source=chatgpt.com)) | Memória prospectiva · working memory | **B/C · moderada/forte** | Controle de estado | Estado existe apenas “na cabeça” → intenção desaparece → trabalho fica incompleto | Status persistente; progresso automático; lembretes vinculados ao objeto; critérios DoD | **O sistema deve ser memória externa do estado operacional. E** |
| **GP-08** | **Detectar desvios e adaptar** | Criar alternativas e responder a imprevistos | Flexibilidade cognitiva; alternar conjunto mental sem perder objetivo | Evidência de dificuldade de set-shifting existe, mas é menos uniforme que atenção/organização | Não é um sintoma clínico específico isolado em NIMH/NICE; deve ser tratado como domínio neuropsicológico, não característica obrigatória | Estudos em adultos encontraram dificuldades específicas de set-shifting; resultados na literatura permanecem heterogêneos. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/22613368/?utm_source=chatgpt.com)) | Flexibilidade cognitiva · set shifting | **B/C · moderada** | Replanejamento | Mudança inesperada exige reconstrução mental do plano → perda de contexto/dependências | Branches pré-calculados; alternativas limitadas; dependências preservadas; retorno ao ponto anterior | **Permitir não-linearidade controlada, não navegação caótica. E** |
| **GP-09** | **Comunicação e stakeholders** | Manter partes alinhadas, registrar decisões e follow-up | Atenção, memória prospectiva, inibição, recuperação contextual | Esquecimento, distração e impulsividade podem interferir na continuidade comunicacional | NIMH inclui esquecimento, distração e interrupção/impulsividade entre manifestações possíveis. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Evidência de memória prospectiva e controle executivo oferece mecanismo plausível. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/23484020/?utm_source=chatgpt.com)) | Memória prospectiva · inibição · atenção | **C + E para efeito específico em PM** | Follow-up | Informação espalhada → necessidade de reconstrução de contexto → decisões e compromissos perdidos | Comunicação associada ao objeto; resumos; decisões persistidas; follow-up convertido em ação | **Centralizar contexto é mais importante que simplesmente adicionar chat. E** |
| **GP-10** | **Finalização e avaliação** | Confirmar entrega, comparar objetivo × resultado, retrospectiva | Fechamento, autocontrole, avaliação do próprio desempenho | Dificuldade em finalizar projetos + potenciais diferenças metacognitivas | NIMH descreve dificuldade em terminar projetos. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Estudo de metacognição em adultos encontrou falta de correspondência entre avaliações subjetivas e objetivas em alguns domínios. ([Springer](https://link.springer.com/article/10.1007/s00702-020-02293-w?utm_source=chatgpt.com)) | Metacognição · self-monitoring | **B/C · moderada** | Closure | “Parece pronto” ≠ critério objetivo → fechamento inconsistente | DoD explícito; evidência anexada; validação; retrospectiva estruturada | **DONE deve ser uma transição verificável, não uma sensação de conclusão. E** |
| **GP-11** | **Capacidade e forecasting** | Planejar recursos/prazo e proteger compromisso de entrega | Autoavaliação, previsão temporal e planejamento | Má gestão temporal é documentada; desalinhamento metacognitivo é possível, não universal | NIMH documenta problemas de planejamento/tempo; não afirma “incapacidade de estimar capacidade produtiva”. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) | Evidência de percepção temporal e metacognição sustenta cautela com estimativas subjetivas, mas não valida diretamente seu algoritmo. ([PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9962130/?utm_source=chatgpt.com)) | Metacognição · previsão · temporalidade | **C para vulnerabilidade; E para solução** | Compromisso de capacidade | “horas livres” confundidas com output → excesso de compromisso | Throughput, cycle time e histórico individual; forecast probabilístico; EB separado de tempo | **Sua arquitetura ****EB = ação****, tempo = medida observada é defensável como decisão de operações, não como tratamento clínico. E** |

# **3. A RELAÇÃO FICA MAIS CLARA QUANDO VISTA COMO SISTEMA**

A síntese é esta:

GESTÃO DE PROJETOS

        │

        │ exige

        ▼

OPERAÇÕES COGNITIVAS

        │

        ├── planejar

        ├── organizar

        ├── priorizar

        ├── sequenciar

        ├── lembrar

        ├── iniciar

        ├── sustentar atenção

        ├── estimar/acompanhar tempo

        ├── monitorar

        ├── adaptar

        └── finalizar

        │

        ▼

TDAH

pode aumentar a vulnerabilidade

em parte desses domínios

        │

        ▼

ATRITO OPERACIONAL

        │

        ├── início tardio

        ├── planejamento incompleto

        ├── prioridades instáveis

        ├── múltiplos trabalhos abertos

        ├── esquecimento de intenções

        ├── perda de contexto

        ├── atraso

        └── fechamento incompleto

        │

        ▼

ARQUITETURA COMPENSATÓRIA

        │

        ├── externalizar

        ├── decompor

        ├── priorizar

        ├── ordenar

        ├── lembrar

        ├── limitar WIP

        ├── mostrar estado

        ├── registrar histórico

        └── prever com dados observados

        │

        ▼

MAIOR FRAÇÃO DA CAPACIDADE COGNITIVA

DISPONÍVEL PARA EXECUÇÃO

A última seta é **E · hipótese de produto**. Ainda precisa ser testada empiricamente; a literatura não permite, neste estágio, afirmar que seu sistema necessariamente “liberará X% de capacidade cognitiva”.

# **4. SUA TESE, AGORA COM CORREÇÕES EPISTÊMICAS**

Seu documento propõe:

priorização → sistema prioriza;
memória de trabalho → reduzir variáveis;
inicialização → reduzir complexidade;
tempo → flexibilizar;
planejamento de longo prazo → ciclos;
troca de contexto → agrupar;
centralização → reduzir dispersão.

Depois da pesquisa, eu classificaria assim:

| **Hipótese original** | **Estado após pesquisa** |
| --- | --- |
| **Dificuldades de planejamento/organização são relevantes no TDAH adulto** | **Sustentado — C** ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) |
| **Gestão de tempo pode ser problemática** | **Sustentado — C** ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)) |
| **Atenção sustentada pode prejudicar execução prolongada** | **Sustentado — B/C** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/26206605/?utm_source=chatgpt.com)) |
| **Memória prospectiva pode afetar follow-through** | **Sustentado — B** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/23484020/?utm_source=chatgpt.com)) |
| **Flexibilidade/set-shifting pode ser afetada** | **Sustentado com heterogeneidade — B/C** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/22613368/?utm_source=chatgpt.com)) |
| **Autoavaliação cognitiva sempre é imprecisa no TDAH** | **Não sustentado como universal**; há evidência de diferenças metacognitivas, mas não uma regra universal. ([Springer](https://link.springer.com/article/10.1007/s00702-020-02293-w?utm_source=chatgpt.com)) |
| **Sistema deve automaticamente priorizar** | **E · decisão de produto plausível**, não conclusão clínica |
| **Sistema deve usar WIP=1** | **E · política de arquitetura**, não prescrição clínica |
| **Impressão/analógico corrige memória de trabalho** | **E · hipótese de design**, ainda precisa ser validada |
| **Ciclos fixos corrigem planejamento de longo prazo** | **E · hipótese de produto**, não resultado clínico demonstrado |
| **Throughput histórico deve substituir percepção subjetiva de capacidade** | **E · forte decisão de operações**, mas precisa ser validada no produto |

Essa separação é importante porque seu próprio documento já propõe **não confundir horas disponíveis com capacidade produtiva** e calibrar throughput/cycle time por execução observada. Ele também corretamente separa EB = ação de Q30 = capacidade temporal, deixando a duração real como variável observada.

# **5. CONCLUSÃO DE PRODUTO / DESIGN**

A conclusão mais defensável **não** é:

“Pessoas com TDAH não conseguem gerir projetos.”

É:

**A gestão convencional de projetos transfere ao operador humano uma quantidade relevante de funções de planejamento, organização, memória prospectiva, atenção, gestão temporal e autocontrole. Alguns desses mesmos domínios apresentam vulnerabilidades estatisticamente documentadas em adultos com TDAH. Portanto, existe fundamento para investigar uma arquitetura de gestão que externalize e automatize parte dessas operações, preservando decisão e autonomia do usuário.**

Isso é muito mais forte cientificamente.

E gera uma tese arquitetural:

### **O usuário executa. O sistema sustenta a execução.**

| **Operação tradicionalmente humana** | **Sistema pode assumir/assistir** |
| --- | --- |
| lembrar tudo | **memória externa persistente** |
| decompor projeto | **decomposição assistida** |
| recalcular prioridade | **motor de prioridade** |
| escolher continuamente o próximo passo | **next action** |
| reconstruir contexto | **estado/contexto persistente** |
| estimar capacidade intuitivamente | **throughput observado** |
| lembrar prazo | **sistema temporal** |
| acompanhar dependências | **grafo/dependency engine** |
| perceber progresso | **progressão visual automática** |
| saber se acabou | **DoD verificável** |
| reorganizar após interrupção | **retomada do estado anterior** |
| abrir múltiplas superfícies | **centralização por objeto** |

O NICE inclusive reconhece **modificações ambientais** como parte relevante da redução do impacto funcional do TDAH e menciona exemplos como reduzir períodos contínuos de foco e reforçar informação verbal com informação escrita. Isso **não valida diretamente essas features digitais**, mas fortalece o princípio de que o ambiente pode ser configurado para reduzir demandas desnecessárias sobre o indivíduo. ([Nice](https://www.nice.org.uk/guidance/ng87/chapter/recommendations?utm_source=chatgpt.com))

Portanto, o seu conceito de **neurodesign não deveria ser “simplificar uma UI para TDAH”**. A formulação tecnicamente mais relevante é:

**transferir carga executiva evitável do operador para o sistema.**

E isso encaixa diretamente na arquitetura do documento-base: cadeia única de objetos e dependências, decomposição até ação observável, estado persistente, redução de alternâncias e capacidade inferida a partir da execução real, não da expectativa subjetiva.

### **Classificação final**

**C · Publicado:** existe sobreposição relevante entre demandas cognitivas da gestão de projetos e domínios em que adultos com TDAH podem apresentar dificuldades. ([NIMH](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know))

**E · Inferido:** um sistema que absorva planejamento repetitivo, memória operacional externa, priorização, controle de estado e forecasting **pode reduzir fricção operacional**.

**Ainda não verificado:** que essa arquitetura produza aumento mensurável de execução, conclusão ou produtividade em usuários com TDAH. Esse é precisamente o claim que o produto deverá testar.