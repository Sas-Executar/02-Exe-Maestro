---
id: DOC-CLX-040
folder_id: FS-OPS-011
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "runbook-geracao-escala.md"
sha256: c181359d25f25c2e79b5b8d157c57e171366ac2003758ff87c9862ce674cec97
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# Runbook de Geração em Escala, Montagem e Pós-Produção

> Consulte este arquivo nos passos 8-10 do workflow (rodar a geração, montar, exportar). Pressupõe que o registro de 25 colunas (passo 6) e os prompts self-contained (passo 7) já foram gerados e validados por `scripts/validar_registro_tsk.py`.

## Passo 8 — Geração em escala

### Ordem de execução

1. **Todas as linhas de keyframe primeiro**, agrupadas por `cluster_id` (processar um bloco/cena inteiro por vez ajuda a manter consistência visual entre planos vizinhos).
2. Dentro de um cluster, respeitar a ordem de `fonte_id`/timing (`start_tc`) do plano de origem — planos adjacentes tendem a se beneficiar de serem gerados em sequência, não em ordem aleatória.
3. **Revisão humana obrigatória de cada keyframe** contra o checklist de `geist-guardrail.md#checklist-rápido` antes de mudar seu `status` para `Concluída e verificada`. Nunca promover automaticamente `Declarada como concluída — não verificada` → `Concluída e verificada` sem essa checagem.
4. Só depois de um keyframe estar `Concluída e verificada`, sua linha de movimento correspondente pode sair de `Bloqueada` e iniciar a geração.
5. Linhas com `status: Não pronta para execução` (claim-check pendente) ficam de fora desta rodada de geração — retornar a elas só depois de o claim ser resolvido (aprovado ou reescrito).

### Tratamento de falha/retry

- Falha de geração (erro de API, output ilegível, output claramente fora do guardrail) → manter `status` em `Em andamento`, registrar a tentativa e o motivo da falha, tentar novamente com o mesmo prompt antes de editar o prompt.
- Se 2-3 tentativas falharem no mesmo prompt, revisar o prompt self-contained (não o modelo) — provavelmente falta especificidade em `<objetivo>` ou `<restricoes>`.
- Nunca "forçar aprovação" de um asset fora do guardrail só para não atrasar o cronograma — isso quebra a regra obrigatória 3 do `SKILL.md` (`existing ≠ approved`).

### Escolha de modelo

Ver `modelos-geracao-video.md`. Registrar a escolha final (modelo + versão + data) como uma linha de `DECISION` visível no relatório de execução (ver formato abaixo) — não apenas na cabeça de quem está operando o pipeline.

## Passo 9 — Montagem seguindo timing/transições da decupagem

- A decupagem original é a **fonte de verdade de timing** — usar `start_tc`, `end_tc`, `duration_seconds`, `transition_in`, `transition_out` de cada plano exatamente como registrados, tanto no registro de 25 colunas quanto na montagem final.
- Ordem de montagem = ordem de `start_tc` dentro de cada `video_id`, sem reordenar planos por "achar que fica melhor" — qualquer reordenação é uma `DECISION` que precisa ser registrada e, idealmente, aprovada pelo usuário antes de executar.
- Se um clipe gerado tiver duração diferente da `duration_seconds` original (ex.: o modelo de geração só produz múltiplos de 4s), ajustar por corte/loop controlado documentando isso como `DECISION`, nunca esticar/comprimir o clipe de forma a distorcer o movimento sem registrar.
- Transições (`transition_in`/`transition_out`) devem ser reproduzidas na edição final exatamente como descritas na decupagem — se a decupagem não especificar um tipo exato de transição, usar corte seco como padrão e registrar como `ASSUMPTION`.

## Passo 10 — Pós-produção e exportação MP4

Checklist final antes de exportar (bloqueante — não exportar até todos os itens estarem `sim`):

- [ ] Todo plano do vídeo tem linha de keyframe **e** linha de movimento em `status: Concluída e verificada`.
- [ ] Nenhuma linha do vídeo está em `Não pronta para execução` (claim pendente) ou `Bloqueada`.
- [ ] Todo `CLAIM-XX` usado no vídeo está em status `APROVADO` (não `NOVO-CANDIDATO`) — a exportação final é o ponto em que candidatos precisam ter sido promovidos.
- [ ] Checklist do `geist-guardrail.md` passou em amostragem do vídeo montado (não só nos keyframes isolados) — cores, tipografia e transições seguem coerentes quando vistas em sequência.
- [ ] Timing total do vídeo montado bate com a soma das durações da decupagem original, salvo `DECISION` registrada para cada desvio.
- [ ] Áudio (quando houver `executar_audio_direction`) está sincronizado com os cortes/transições correspondentes.

## Formato do relatório de execução

Ao final dos passos 8-10, entregar um relatório com, no mínimo:

```
Vídeo: [video_id]
Modelo(s) de geração usado(s): [nome + versão + data da escolha]
Total de planos: [N] | Total de linhas TSK: [N x 2]

Por tarefa_id:
  TSK-NNNN | status final | path/link do asset | claim(s) associado(s) e status

Claims pendentes de promoção (se houver): [lista de CLAIM-XX NOVO-CANDIDATO]
Desvios de timing/transição registrados como DECISION (se houver): [lista]
Conflitos registrados (se houver): [lista de CONF-XX]
```

Este relatório não substitui o registro de 25 colunas — é um resumo de execução para o usuário acompanhar o estado do pipeline sem abrir o CSV inteiro.
