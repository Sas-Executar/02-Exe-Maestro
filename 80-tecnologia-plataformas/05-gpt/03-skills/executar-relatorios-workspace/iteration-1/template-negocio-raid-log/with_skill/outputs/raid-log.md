---
title: "RAID Log — Projeto de Migração de Dados"
template: execution/raid-log
visual_profile: register
status: DEMO / CONTEUDO FICTICIO — dados inventados para teste, sem fonte real
projeto: "Migração de Dados — Plataforma Legada para Novo Ambiente Cloud"
data_geracao: 2026-09-23
preparado_para: "Reunião de amanhã (24/09/2026)"
---

# RAID Log — Projeto de Migração de Dados

> **Aviso:** este documento é um exemplo de demonstração. Todo o conteúdo
> abaixo (riscos, premissas, issues, dependências, owners e prazos) é
> fictício, criado para fins de teste da skill `executar-relatorios`. Não
> reflete um projeto real e não deve ser usado para decisões operacionais.

**Projeto:** Migração de Dados — Plataforma Legada para Novo Ambiente Cloud
**Sponsor:** Não identificado no documento (dado fictício não atribuído)
**Última atualização:** 2026-09-23

---

## 1. Risks (Riscos)

| ID | Risco | Probabilidade | Impacto | Owner | Ação de mitigação | Prazo |
|----|-------|---------------|---------|-------|--------------------|-------|
| R01 | Perda ou corrupção de dados durante a transferência do banco legado para o novo cluster cloud | Média | Alto | Ana Ribeiro (Eng. de Dados) | Executar checksum e reconciliação de contagem de registros em cada lote antes do cutover | 2026-10-03 |
| R02 | Janela de indisponibilidade do sistema legado maior que o previsto, afetando operação do cliente | Média | Alto | Bruno Castro (Infra) | Testar migração em ambiente de homologação com volume real (dry-run cronometrado) | 2026-09-29 |
| R03 | Divergência de schema entre banco de origem e banco de destino não mapeada previamente | Baixa | Médio | Carla Mendes (Arquitetura de Dados) | Revisão cruzada do mapeamento de schema com time de aplicação | 2026-09-26 |
| R04 | Dependência de fornecedor terceirizado para liberar acesso à API do novo ambiente cloud | Média | Médio | Diego Farias (Compras/Fornecedores) | Escalar contrato e SLA junto ao fornecedor; solicitar confirmação por escrito | 2026-09-30 |
| R05 | Rollback complexo ou inviável em caso de falha crítica pós-migração | Baixa | Alto | Ana Ribeiro (Eng. de Dados) | Manter ambiente legado em modo somente-leitura por 15 dias após cutover como plano de contingência | 2026-10-10 |

## 2. Assumptions (Premissas)

| ID | Premissa | Owner | Validação necessária |
|----|----------|-------|------------------------|
| A01 | O volume total de dados a migrar é de aproximadamente 2,4 TB | Ana Ribeiro | Confirmar com relatório atualizado do DBA antes do cutover |
| A02 | A janela de manutenção aprovada pelo negócio é de 6 horas em um sábado à noite | Bruno Castro | Confirmar com stakeholders de operação até 2026-09-27 |
| A03 | Todas as equipes downstream (BI, faturamento, atendimento) já foram notificadas do congelamento de dados durante a migração | Diego Farias | Confirmar envio de comunicado oficial |
| A04 | O ambiente de homologação replica fielmente o volume e a estrutura de produção | Carla Mendes | Validar com auditoria de configuração antes do dry-run |

## 3. Issues (Problemas em aberto)

| ID | Issue | Severidade | Owner | Status | Próximo passo |
|----|-------|------------|-------|--------|----------------|
| I01 | Script de transformação (ETL) ainda apresenta falhas intermitentes ao converter campos de data legados | Alta | Carla Mendes | Em andamento | Corrigir parser de datas e reexecutar suite de testes até 2026-09-25 |
| I02 | Acesso de leitura ao ambiente cloud de destino ainda não foi liberado para o time de QA | Média | Diego Farias | Bloqueado | Escalar com fornecedor de infraestrutura; prazo limite 2026-09-26 |
| I03 | Falta de ambiente de staging dedicado para o teste de carga final | Média | Bruno Castro | Em andamento | Provisionar staging até 2026-09-28 |

## 4. Dependencies (Dependências)

| ID | Dependência | Tipo | Depende de | Owner | Impacto se atrasar |
|----|-------------|------|------------|-------|----------------------|
| D01 | Liberação de acesso à API do novo ambiente cloud | Externa (fornecedor) | Fornecedor de infraestrutura | Diego Farias | Bloqueia início do dry-run completo |
| D02 | Conclusão da correção do script de ETL (I01) | Interna | Time de Engenharia de Dados | Carla Mendes | Bloqueia validação final de qualidade de dados |
| D03 | Aprovação formal da janela de manutenção pelo Comitê de Mudanças | Interna (governança) | Comitê de Change Management | Bruno Castro | Bloqueia agendamento do cutover |
| D04 | Confirmação do plano de comunicação com áreas downstream | Interna | Time de Comunicação/PMO | Diego Farias | Risco de impacto não comunicado a usuários finais |

## 5. Owner (Responsáveis)

| Nome | Papel no projeto |
|------|-------------------|
| Ana Ribeiro | Engenharia de Dados — execução técnica da migração |
| Bruno Castro | Infraestrutura — ambiente, janela de manutenção, staging |
| Carla Mendes | Arquitetura de Dados — schema, ETL, qualidade de dados |
| Diego Farias | Compras/Fornecedores e Comunicação — dependências externas |

## 6. Next Action (Próxima ação)

Revisar este RAID log na reunião de 24/09/2026, confirmar owners e prazos
com cada responsável, e priorizar o desbloqueio de I02 (acesso ao ambiente
cloud) e D01, que atualmente travam o cronograma de dry-run.

## 7. Due Date (Prazo geral do projeto)

**Cutover planejado (fictício):** 2026-10-04
**Data desta revisão:** 2026-09-23
**Próxima revisão do RAID log:** 2026-09-30 (ou antes, se um item de severidade Alta mudar de status)

---

*Documento gerado como demonstração da capacidade "pacote de templates de
negócio" da skill `executar-relatorios`, a partir do template
`templates/execution/raid-log.md` (perfil visual: `register`). Nenhum dado
acima corresponde a um projeto real.*
