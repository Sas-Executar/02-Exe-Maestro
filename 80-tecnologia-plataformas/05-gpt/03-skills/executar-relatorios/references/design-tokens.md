# Contrato de tokens de design

**Este arquivo descreve o CONTRATO estrutural de tokens. Os valores concretos
(cores, espaçamento, temas) aguardam o novo contrato de tokens do usuário e
devem ser preenchidos em `assets/tokens/` antes de qualquer renderização
visual.**

Não hardcode hex, nem em CSS, nem em SVG, nem em prosa de referência, enquanto
esse preenchimento não acontecer. Onde um valor concreto é necessário para o
artefato funcionar (ex.: `:root` de um template), use um marcador `/* A
DEFINIR */` — nunca um palpite.

## De onde vem esse contrato

Esta skill herdou um stack de tokens de uma extração visual anterior
(família "Executar Playbook"). Essa extração se declarava `REFERENCE_ONLY`:
boa parte dos itens não tinha valor físico recuperável, e toda a geometria
de origem estava em `px-image` — pixel de uma imagem de referência, não
medida física de papel. O arquivo de extração bruta não foi trazido para
este pacote; só a estrutura conceitual permanece, documentada aqui e em
`assets/tokens/tokens.schema.json`.

Isso importa porque muda como qualquer valor futuro deve ser tratado: uma cor
medida é um fato; uma margem "de 28px" sobre uma imagem não é fato nenhum
sobre papel até alguém decidir e registrar a base do cálculo.

## As três camadas

```
raw        valor primitivo (cor medida, número bruto). Nenhum componente
           consome esta camada diretamente.
  ↓
alias      o que o componente consome: --exec-color-brand, --exec-space-4…
  ↓
componente o que cada peça usa: field.placeholder, check.box, kpi.value…
```

A camada alias existe para que trocar o acento visual seja uma linha, e não
uma caçada por valor espalhado pelo arquivo. Regra que sustenta isso:
**acento é sempre presentacional, nunca estrutural.** Trocar cor não pode
mexer em hierarquia, grade ou dado.

## Proveniência: todo item declara de onde veio

Cada entrada em um futuro `assets/tokens/tokens.json` deve carregar `origem`
e `base`, seguindo `assets/tokens/tokens.schema.json`:

| origem | significa | o que se pode fazer |
|---|---|---|
| `FONTE` | medido ou observado na fonte de design atual | usar como está |
| `DECISAO` | a fonte deixou indefinido e esta camada fixou um valor | usar, mas ler a `base` antes de mudar |
| `LACUNA` | continua indefinido | **decidir e registrar antes de usar** — o validador deve acusar se vazar para um artefato |

Todo `DECISAO` carrega, em `base`, o cálculo ou critério que justificou o
valor — nunca um número solto sem explicação.

## Validação de contraste

Qualquer par texto/fundo precisa atender:
- **≥ 4,5:1** para texto normal (corpo, placeholder, título);
- **≥ 3:1** para objeto gráfico (contorno de checkbox, borda de campo,
  rótulo puramente decorativo).

`scripts/tokens.py --contraste` recalcula essa tabela assim que
`assets/tokens/tokens.json` existir. Nenhum tema deve ser considerado pronto
sem essa checagem passando.

## Temas: sobreposição, não reescrita

Um tema é uma sobreposição de valores na camada alias — nunca cria token
novo, nunca mexe em grade, geometria ou hierarquia. Se um tema precisar
mudar layout, ele não é tema: é outro contrato de peça, e o lugar dele é em
`references/workbook/contrato-workbook.md`.

A forma esperada de `assets/tokens/temas.json` está em
`assets/tokens/temas.schema.json`. Nomes de tema específicos (a família
anterior usava `playbook`/`swiss`/`editorial`) não são parte deste contrato;
o novo contrato de tokens do usuário define quais temas existem.

## Unidades

- Em SVG A4, o `viewBox` é `0 0 210 297`: 1 unidade de usuário = 1mm. Isso é
  geometria de página, não decisão de marca — permanece fixo.
- Nenhuma medida em `px-image` (ou equivalente de uma extração visual) vira
  mm, pt ou px de CSS por conversão silenciosa. Toda medida física é uma
  `DECISAO` registrada com a base do cálculo.
- Escala de espaço fechada (herdada da família anterior, reaproveitável):
  1 · 2 · 3 · 4 · 6 · 8 · 12 · 16 · 24 · 32 mm. Um valor fora da escala é
  sinal de que alguém mediu na tela em vez de decidir.

## Dois vocabulários de raio

Sempre que existe objeto de identidade e chrome de interação na mesma peça,
eles não compartilham raio — mesmo que o valor numérico ainda não esteja
definido:

- raio de artefato (cards, pranchas — o que é do produto);
- raio de controle (botão, pílula, trilha de barra — sempre cápsula/circular);
- raio de checkbox (quase reto de propósito: arredondado demais lê como
  botão, e ninguém escreve dentro de um botão).

## Como preencher quando o novo contrato chegar

1. Escreva `assets/tokens/tokens.json` seguindo
   `assets/tokens/tokens.schema.json` (raw → alias → componente, com
   `origem`/`base` em cada item).
2. Escreva `assets/tokens/temas.json` (se houver mais de um tema) seguindo
   `assets/tokens/temas.schema.json`.
3. Rode `python3 scripts/tokens.py --contraste --lacunas` — nenhuma
   reprovação, nenhuma lacuna aberta antes de usar em produção.
4. Rode `python3 scripts/tokens.py --sincronizar assets/templates/*.{svg,html}`
   para reescrever os blocos `/* TOKENS:INICIO */ … /* TOKENS:FIM */`.
5. Substitua os marcadores `/* A DEFINIR */` e "A DEFINIR — aguardando
   contrato de tokens" em `assets/report.css`, `references/40-visual-system.md`
   e nos templates de `assets/templates/`.
6. Regere e valide os artefatos (`scripts/validar_artefato.py`,
   `scripts/gerar_workbook.py`, `scripts/gerar_relatorio.py`).
