# Projeções do Mapa-OS

Toda projeção lê o mesmo `mapa_os` validado. Nenhuma projeção cria objeto, promove estado, resolve conflito ou reordena dependências por estética.

## mapa_operacional

Mostre posição, progresso sustentado, ação Agora, critério de conclusão, evidência necessária, bloqueios, itens Próximo/Depois e a pergunta: “A prova descrita existe?”.

## agora_proximo_depois

Agrupe por horizonte, preservando IDs e prazos. Um prazo original vencido permanece registrado; uma nova previsão é outro campo. O bloco Agora recebe WIP=1.

## status_terminal

Síntese compacta: header, progresso por profundidade, posição atual, 3P+N, riscos, prevenção, evidências e tags. Percentuais exigem numerador/denominador explícitos.

## prisma_7d

Use somente quando houver dados suficientes para sete dias ou quando o usuário autorizar planejamento desses sete dias. Converta o Mapa-OS em payload conforme `schemas/prism-report.schema.json`: Face 01 com uma épica, intenção, progresso e quatro KPIs; Face 02 com sete dias; Face 03 com um entregável principal, quatro entregáveis de apoio e próximo estado.

O template `assets/templates/status-report-prisma-a4-v4.html` é fixo. Os 100 placeholders pertencem apenas aos namespaces `DOC_*`, `EPIC_*`, `CALENDAR_*` e `RESULT_*`. Não reintroduza tokens legados.

Quando um campo exceder `maxLength`, remova redundância e condense sem perder IDs, datas, quantidades, milestones ou qualificadores de estado. Nunca reduza tipografia, margens, paddings ou faces. Se não couber sem perda, retorne erro de fit.

```bash
python scripts/render_prism.py payload.json output.html
python scripts/audit_prism.py
```
