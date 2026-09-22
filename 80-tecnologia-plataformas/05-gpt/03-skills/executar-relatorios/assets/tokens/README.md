# assets/tokens/ — aguardando novo contrato de tokens do usuário

Esta pasta não contém valores concretos de cor, espaçamento ou tema.

- `tokens.schema.json` — forma esperada de `tokens.json` (raw → alias →
  componente, com proveniência `FONTE`/`DECISAO`/`LACUNA` por item).
- `temas.schema.json` — forma esperada de `temas.json` (sobreposições de
  tema na camada alias).

Quando o novo contrato de tokens chegar, crie `tokens.json` e (se houver mais
de um tema) `temas.json` nesta pasta seguindo esses schemas. Depois rode
`python3 scripts/tokens.py --contraste --lacunas` antes de gerar qualquer
artefato visual.

Ver `references/design-tokens.md` para o contrato completo.
