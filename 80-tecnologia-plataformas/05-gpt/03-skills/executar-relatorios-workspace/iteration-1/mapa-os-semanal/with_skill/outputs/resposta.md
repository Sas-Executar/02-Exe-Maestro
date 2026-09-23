> **Nota de execução deste teste:** esta é uma simulação. Não houve uma pessoa real para entrevistar, então as respostas abaixo (identidade do projeto, prazos, capacidade semanal, entregas/fluxos/ações e evidências) foram **inventadas para exercitar o fluxo "01 — quero criar meu mapa da semana"** com um caso plausível (fundadora solo lançando uma landing page). Nenhum dado aqui deve ser tratado como fato de um projeto real.

---

## Coleta progressiva (simulada)

**Bloco 1 — projeto, semana, objetivo**
- Projeto: Landing page de lançamento — Aurora Co
- Owner: Marina Duarte (fundadora solo)
- Semana: W39, 2026-09-21 a 2026-09-27
- Objetivo da semana: publicar a landing page no domínio próprio e validar a captura de e-mails antes da divulgação pública.

**Bloco 2 — problema, processo, progresso sustentado**
- Problema: a página ainda não está publicada nem validada publicamente.
- Processo: copy → montagem → publicação → captura de e-mail → divulgação, uma ação ativa por vez.
- Progresso sustentado: copy finalizada e aprovada; página já montada no builder (Framer), com captura de tela como evidência.

**Bloco 3 — capacidade e restrições**
- Segunda a sexta: ~3h/dia; sábado: ~2h; domingo: 0h.
- Restrição fixa: manhãs reservadas para trabalho com clientes.

**Bloco 4 — entregas, fluxos, ações, evidências, bloqueios**
- Uma entrega (Landing page publicada e validada) → um fluxo (Construção e publicação) → cinco ações em cadeia de dependência (copy → montagem → publicação → captura de e-mail → divulgação).
- Evidências: documento de copy aprovado (D_INTERNO) e captura de tela da página montada (A_OBSERVADO).
- Bloqueios: nenhum bloqueio ativo. Lacuna registrada: o prazo original foi informado apenas de forma aproximada ("fim da semana"), sem previsão atual distinta.

---

# DOCUMENT READER · VALU-MODE V3

| Campo | Valor |
|---|---|
| ID | OPS-MAPA-AURORA-LP-W39 |
| Tipo | Mapa-OS semanal (EXECUTAR) |
| Owner | Marina Duarte |
| Versão | 1.0 |
| Data | 2026-09-23 |
| Fase | Construção e publicação |
| Projeto | PRJ-001 — Landing page de lançamento — Aurora Co |
| PARA | Marina Duarte (fundadora) |
| Referência | SRC-INTERVIEW-001 (dados simulados) |
| 3# | #landing-page #lancamento #semana-w39 |

## RESUMO EXECUTIVO

- **O quê:** mapa operacional da semana W39 para a landing page de lançamento da Aurora Co.
- **Por quê:** a página ainda não foi publicada nem validada publicamente; é preciso destravar essa etapa antes de configurar captura de e-mail e divulgar.
- **Quem:** Marina Duarte, fundadora solo.
- **Como:** WIP=1 — uma entrega ativa (Landing page publicada e validada), um fluxo ativo (Construção e publicação) e uma única ação ativa por vez, seguindo a cadeia de dependências.

## 3P+N · APLICAÇÃO

- **Problema:** a landing page de lançamento ainda não foi publicada nem validada publicamente antes do lançamento.
- **Processo:** concluir copy e montagem, publicar no domínio próprio, configurar captura de e-mail e só então divulgar — uma ação ativa por vez.
- **Progresso:** copy finalizada e página montada no builder (Framer); publicação pública ainda pendente.
- **Next:** publicar a landing page no domínio próprio e confirmar acesso público.

## Posição operacional

- Modo: EXECUTAR
- Entrega ativa: DLV-001 — Landing page publicada e validada
- Fluxo ativo: FLW-001 — Construção e publicação da página
- Ação ativa: **ACT-003 — Publicar no domínio próprio**

## Única próxima ação

- **ACT-003 — Publicar no domínio próprio**
- Instrução: publicar a landing page no domínio próprio (aurora.co) e confirmar acesso público.
- Critério de conclusão: página acessível publicamente no domínio, sem erros de carregamento.
- Evidência necessária: captura de tela ou link ativo confirmando a publicação.
- Autoridade: DETERMINISTICO (única ação elegível — dependência ACT-002 já implementada, sem bloqueio ativo).

## Evidência

- EVID-001 (D_INTERNO): documento de copy revisado e aprovado — sustenta ACT-001.
- EVID-002 (A_OBSERVADO): captura de tela da página montada no builder — sustenta ACT-002.

## Bloqueios e lacunas

- Nenhum bloqueio ativo no momento.
- Lacuna registrada (severidade *info*): o prazo original de publicação foi informado apenas de forma aproximada ("fim da semana"); não há previsão atual (`current_forecast`) distinta registrada. Não impede a geração do mapa; fica sinalizada para confirmação futura.

## Horizontes

- **Agora:** ACT-003 — Publicar no domínio próprio.
- **Próximo:** ACT-004 — Configurar captura de e-mail (Mailchimp), elegível após ACT-003.
- **Depois:** ACT-005 — Divulgar em 3 canais (Instagram, LinkedIn, comunidade), elegível após ACT-004.

## Arquivos gerados

- `mapa-os-output.json` — objeto canônico validado contra `schemas/output.schema.json`.
- `resposta.md` — esta resposta em linguagem simples (Document Reader).

Não foi gerado, neste teste, o payload/HTML do Prisma A4 de três faces (`prisma_7d`); o escopo pedido para esta execução foi limitado ao JSON canônico e à resposta legível. A projeção registrada no JSON é `agora_proximo_depois`, estado `validated`.

## Resultado da validação

```
$ python3 scripts/validate_mapa.py mapa-os-output.json
PASS
```

- Schema válido: sim.
- WIP válido: sim (uma entrega ativa, um fluxo ativo, uma ação ativa).
- Dependências válidas: sim.
- Evidências válidas: sim (toda ação em estado que exige evidência — `implemented` — tem `evidence_refs` correspondente).

## Nível realmente alcançado

**Validado.** O JSON canônico foi criado e passou na validação automatizada (`validate_mapa.py` → `PASS`). Não foi renderizado (nem inspecionado em impressão) nenhum artefato visual/Prisma nesta execução — isso não foi declarado.
