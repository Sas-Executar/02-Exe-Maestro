# RAID Log — Projeto de Migração de Dados (Legacy ERP → Plataforma Cloud)

**Documento preparado para:** Reunião de status de amanhã, 24/09/2026
**Responsável pela atualização:** sas.executar@gmail.com
**Última atualização:** 23/09/2026

> Nota: Este é um documento de demonstração/teste com conteúdo fictício e plausível, gerado para fins de exercício. Os riscos, premissas, issues e dependências abaixo não representam dados reais de projeto.

---

## Resumo Executivo

O projeto de migração de dados do ERP legado (on-premise) para a nova plataforma cloud segue em andamento, atualmente na fase de mapeamento e testes de carga (ETL). Este RAID Log consolida os principais riscos, premissas, issues (problemas correntes) e dependências que devem ser discutidos na reunião de amanhã, com foco em decisões pendentes que impactam o cronograma de corte (cutover) previsto.

---

## 1. Riscos (Risks)

| ID | Descrição do Risco | Probabilidade | Impacto | Nível | Mitigação Proposta | Responsável | Status |
|----|---|---|---|---|---|---|---|
| R-01 | Volume real de dados históricos (>15 anos) pode exceder a estimativa inicial, estourando a janela de migração noturna planejada (6h). | Média | Alto | Alto | Executar teste de carga completo com dataset de produção espelhado; avaliar migração incremental por lote (chunking). | Equipe de Engenharia de Dados | Aberto |
| R-02 | Divergências de schema entre o sistema legado e o novo modelo de dados podem gerar perda ou distorção de informações em campos customizados. | Média | Alto | Alto | Mapeamento de campo a campo com validação do time de negócio antes do cutover; criar de-para documentado. | Analista de Dados / Product Owner | Aberto |
| R-03 | Indisponibilidade do fornecedor da plataforma cloud durante a janela de corte (falha de infraestrutura do lado do provedor). | Baixa | Alto | Médio | Confirmar SLA e canal de suporte prioritário com o fornecedor; definir plano B de rollback. | Gerente de Projeto | Aberto |
| R-04 | Resistência de usuários-chave das áreas de negócio à adoção da nova interface, gerando baixa adesão pós-go-live. | Média | Médio | Médio | Plano de change management, treinamentos e comunicação antecipada; identificar champions por área. | RH / Change Management | Em monitoramento |
| R-05 | Equipe técnica sobrealocada em outros projetos simultâneos, podendo atrasar entregas críticas de ETL. | Alta | Médio | Alto | Negociar prioridade formal com liderança; considerar reforço temporário (consultoria externa). | Gerente de Projeto | Aberto |
| R-06 | Qualidade dos dados de origem (duplicidades, registros órfãos) pode comprometer a integridade pós-migração. | Alta | Médio | Alto | Rodada de data cleansing antes da migração final; relatório de qualidade de dados (DQ report). | Equipe de Engenharia de Dados | Em andamento |

---

## 2. Premissas (Assumptions)

| ID | Descrição da Premissa | Impacto se Inválida | Responsável pela Validação | Status |
|----|---|---|---|---|
| A-01 | O ambiente de homologação (staging) da plataforma cloud está disponível e configurado de forma idêntica ao ambiente de produção. | Testes de migração não seriam representativos, exigindo retrabalho. | Infraestrutura / DevOps | Validado |
| A-02 | Todas as áreas de negócio já concluíram o levantamento de requisitos de dados obrigatórios até o final desta semana. | Atraso na fase de mapeamento e no cronograma geral. | Product Owners por área | Pendente |
| A-03 | O fornecedor da plataforma cloud fornecerá suporte técnico dedicado durante a semana do cutover. | Risco elevado de indisponibilidade prolongada sem suporte. | Gerente de Projeto | A confirmar com fornecedor |
| A-04 | Não haverá mudanças regulatórias (ex.: LGPD) que afetem o escopo de dados durante o período de migração. | Necessidade de replanejamento de escopo e possíveis atrasos legais. | Jurídico / Compliance | Validado |
| A-05 | O orçamento aprovado cobre eventuais horas extras de consultoria especializada em ETL. | Necessidade de nova aprovação orçamentária, atrasando a execução. | Sponsor do Projeto | Pendente |

---

## 3. Issues (Problemas Correntes)

| ID | Descrição do Issue | Impacto | Ação em Curso | Responsável | Prazo | Status |
|----|---|---|---|---|---|---|
| I-01 | Script de extração (extract) do módulo financeiro está apresentando timeout em lotes acima de 500k registros. | Bloqueia testes de carga completos do módulo financeiro. | Otimização de query e paralelização do processo de extração. | Dev Sênior de Dados | 26/09/2026 | Em andamento |
| I-02 | Falta de acesso de leitura ao banco de staging para 2 membros da equipe de QA, atrasando a validação de dados migrados. | Atraso nos testes de aceitação (UAT) de dados. | Solicitação de acesso aberta junto à área de Infraestrutura. | Infraestrutura / DevOps | 25/09/2026 | Aberto |
| I-03 | Inconsistência identificada entre o dicionário de dados fornecido pela área de Compras e os campos reais do sistema legado. | Pode gerar mapeamento incorreto de dados críticos. | Reunião de esclarecimento agendada com a área de Compras. | Analista de Dados | 30/09/2026 | Aberto |
| I-04 | Ambiente de testes de performance apresentou lentidão intermitente na última rodada (causa raiz não identificada). | Resultados de teste de carga não são totalmente confiáveis. | Investigação em conjunto com o time de infraestrutura do fornecedor. | Infraestrutura / DevOps | 27/09/2026 | Em investigação |

---

## 4. Dependências (Dependencies)

| ID | Descrição da Dependência | Tipo | De quem depende | Impacto se atrasar | Status |
|----|---|---|---|---|---|
| D-01 | Aprovação final do mapeamento de campos (de-para) pelas áreas de negócio. | Interna | Product Owners de cada área | Bloqueia o início da migração final de produção. | Pendente |
| D-02 | Disponibilização do ambiente de produção da plataforma cloud pelo fornecedor. | Externa | Fornecedor da plataforma cloud | Impede a realização do cutover na data planejada. | Em andamento |
| D-03 | Conclusão da rodada de testes de segurança e penetração (pentest) pela equipe de segurança da informação. | Interna | Segurança da Informação (InfoSec) | Bloqueia o go-live sem aprovação formal de compliance. | Agendado para semana de 06/10/2026 |
| D-04 | Confirmação da janela de indisponibilidade (downtime) autorizada pelas áreas de negócio para o corte final. | Interna | Comitê de Sponsors / Áreas de Negócio | Impossibilita agendamento definitivo do cutover. | Pendente |
| D-05 | Entrega da documentação de APIs de integração pelo fornecedor da plataforma cloud, necessária para os conectores pós-migração. | Externa | Fornecedor da plataforma cloud | Atraso na configuração das integrações downstream. | Em atraso (previsto 20/09, ainda não recebido) |

---

## Itens Prioritários para Discussão na Reunião

1. **R-01 e R-05** — Risco de estouro da janela de migração combinado com sobrealocação da equipe; decisão necessária sobre reforço de equipe ou replanejamento de datas.
2. **I-01** — Bloqueio técnico no módulo financeiro que pode impactar o cronograma de testes desta semana.
3. **D-05** — Atraso do fornecedor na entrega da documentação de APIs; necessário escalonamento formal.
4. **A-02 e A-05** — Duas premissas ainda pendentes de validação que afetam diretamente o planejamento financeiro e de escopo.

---

*Documento gerado como exercício de demonstração (conteúdo fictício). Deve ser revisado e substituído por dados reais do projeto antes de qualquer uso formal.*
