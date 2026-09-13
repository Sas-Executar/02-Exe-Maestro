---
id: DOC-CLX-076
folder_id: FS-DAT-009
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "schemas-oficiais.md"
sha256: d1d1b1075eeab965a8985848699f36c2246ef06288a0677e4a2ee9bbb03be901
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# Schemas oficiais do Claude Code — snapshot verificado

> **Data de verificação:** 2026-07-31, contra `code.claude.com/docs/en/plugin-marketplaces` e páginas relacionadas.
> **Regra de precedência:** a documentação viva sempre vence este arquivo. Este snapshot existe para acelerar o trabalho e para permitir operação offline declarada, não para substituir a Fase 0.

## Índice

1. [Pontos que mudam com frequência](#1-pontos-que-mudam-com-frequência)
2. [Estrutura de diretórios reconhecida](#2-estrutura-de-diretórios-reconhecida)
3. [plugin.json](#3-pluginjson)
4. [marketplace.json](#4-marketplacejson)
5. [Fontes de plugin](#5-fontes-de-plugin)
6. [Frontmatter de SKILL.md](#6-frontmatter-de-skillmd)
7. [Frontmatter de agente](#7-frontmatter-de-agente)
8. [hooks.json](#8-hooksjson)
9. [Variáveis de ambiente](#9-variáveis-de-ambiente)
10. [Nomes reservados de marketplace](#10-nomes-reservados-de-marketplace)

---

## 1. Pontos que mudam com frequência

Confira estes especificamente na Fase 0. São os que mais mudaram em 2026 e os que mais quebram plugins:

| Item | Estado em 2026-07-31 | Por que checar |
|---|---|---|
| `renames` no marketplace | Existe; requer Claude Code ≥ v2.1.193 | Campo novo; versões anteriores ignoram e reportam `plugin-not-found` |
| `displayName` | Existe; requer ≥ v2.1.143 | Recente |
| `defaultEnabled` | Existe; requer ≥ v2.1.154 | Recente |
| `relevance` | Existe; requer ≥ v2.1.152; só vale em marketplaces allowlistados por admin | Escopo restrito, fácil de usar errado |
| Nomes reservados | Lista fechada, rechecada a cada carregamento | A lista cresce. Um nome que funcionava pode parar de funcionar |
| Resolução de versão | `plugin.json` > entrada de marketplace > SHA do commit | Mudou o comportamento de update |
| `monitors/` | Experimental | Pode mudar ou sair |
| Validação de kebab-case | Aviso não bloqueante no CLI, mas **a sincronização do marketplace no claude.ai rejeita** nomes fora do padrão | Divergência entre CLI e claude.ai |

---

## 2. Estrutura de diretórios reconhecida

```
<plugin-name>/
├── .claude-plugin/
│   └── plugin.json          # APENAS isto vive aqui
├── skills/<nome>/SKILL.md   # capacidades por instrução (preferir para plugins novos)
├── commands/*.md            # formato plano, legado/compatibilidade
├── agents/*.md              # subagentes
├── hooks/hooks.json         # automações por evento
├── monitors/monitors.json   # experimental
├── bin/                     # executáveis no PATH do Bash durante o uso
├── .mcp.json                # servidores MCP
├── .lsp.json                # servidores de linguagem
└── settings.json            # apenas chaves suportadas
```

**Regra crítica de cache:** na instalação, o Claude Code copia o diretório do plugin para `~/.claude/plugins/cache`. Qualquer caminho que saia do diretório (`../shared`) deixa de resolver. Para compartilhar arquivos entre plugins, use symlink.

---

## 3. plugin.json

Vive em `.claude-plugin/plugin.json`.

```json
{
  "$schema": "https://json.schemastore.org/claude-code-plugin-manifest.json",
  "name": "meu-plugin",
  "displayName": "Meu Plugin",
  "version": "0.1.0",
  "description": "Faz X para Y produzindo Z.",
  "author": { "name": "Nome" },
  "homepage": "https://...",
  "repository": "https://github.com/owner/repo",
  "license": "MIT",
  "keywords": ["tag-1", "tag-2"]
}
```

| Campo | Obrigatório | Regras |
|---|---|---|
| `name` | Sim | kebab-case, sem espaços. **Imutável após publicação** — define o namespace das skills (`/<plugin>:<skill>`) e é a chave em `enabledPlugins` |
| `displayName` | Não | Rótulo humano; pode ter espaços e maiúsculas; não usado para namespace |
| `version` | Recomendado | Se definido, o plugin fica *pinado*: usuários só recebem atualização quando a string muda. Se omitido em fonte git, cada commit conta como versão nova |
| `description` | Sim, na prática | Deve declarar capacidade, contexto e resultado |
| `author` | Sim | `name` obrigatório; `email` e `url` opcionais |
| `homepage`, `repository`, `license`, `keywords` | Não | **Omita se desconhecido.** Não preencha com placeholder |

**Armadilha de versão:** não defina `version` em `plugin.json` *e* na entrada de marketplace. O Claude Code sempre usa o valor do `plugin.json`, sem avisar, então um manifesto desatualizado mascara a versão do marketplace.

---

## 4. marketplace.json

Vive em `.claude-plugin/marketplace.json`, na raiz do repositório de marketplace.

```json
{
  "name": "meu-marketplace",
  "owner": { "name": "Nome", "url": "https://github.com/owner" },
  "description": "Catálogo de plugins de portfólio.",
  "metadata": { "pluginRoot": "./plugins" },
  "plugins": [
    {
      "name": "meu-plugin",
      "source": "./plugins/meu-plugin",
      "description": "Faz X para Y produzindo Z.",
      "version": "0.1.0",
      "category": "produtividade",
      "tags": ["skills", "automacao"],
      "license": "MIT"
    }
  ],
  "renames": {}
}
```

### Campos obrigatórios do marketplace

| Campo | Tipo | Regras |
|---|---|---|
| `name` | string | kebab-case. Público — o usuário vê em `/plugin install X@<name>`. Um usuário só registra **um** marketplace por nome; adicionar outro com o mesmo nome substitui o primeiro |
| `owner` | objeto | `name` obrigatório; `email` e `url` opcionais |
| `plugins` | array | Lista de entradas |

### Campos opcionais relevantes

| Campo | Utilidade |
|---|---|
| `metadata.pluginRoot` | Prefixo dos caminhos relativos. Com `"./plugins"`, a entrada pode usar `"source": "meu-plugin"` |
| `renames` | Mapa `nome-antigo → nome-novo` ou `→ null` se removido. Trate como histórico **append-only**: nunca edite entrada antiga, adicione nova. O validador rejeita ciclos e cadeias que não terminam |
| `allowCrossMarketplaceDependenciesOn` | Só quando houver dependência entre marketplaces |

### Entrada de plugin

Aceita **qualquer campo do manifesto** mais os específicos de marketplace: `source` (obrigatório), `category`, `tags`, `strict`, `relevance`.

**`strict`:**

| Valor | Comportamento |
|---|---|
| `true` (padrão) | `plugin.json` é a autoridade; a entrada de marketplace pode acrescentar componentes. Os dois são mesclados |
| `false` | A entrada de marketplace é a definição completa. Se o plugin também tiver `plugin.json` declarando componentes, isso é conflito e o plugin falha ao carregar |

Para o portfólio, use `strict: true` (padrão) — cada plugin deve ser autônomo e instalável mesmo fora do marketplace.

---

## 5. Fontes de plugin

| Fonte | Forma | Observação |
|---|---|---|
| Caminho relativo | `"./plugins/meu-plugin"` | Deve começar com `./`. Resolve contra a raiz do marketplace, **não** contra `.claude-plugin/`. Proibido usar `..`. **Não funciona em marketplace adicionado por URL direta ao JSON** |
| `github` | `{"source":"github","repo":"owner/repo","ref":"?","sha":"?"}` | `sha` completo de 40 caracteres quando usado |
| `url` | `{"source":"url","url":"https://...","ref":"?","sha":"?"}` | Qualquer host git |
| `git-subdir` | `{"source":"git-subdir","url":"...","path":"tools/plugin"}` | Clone esparso; bom para monorepo |
| `npm` | `{"source":"npm","package":"@org/plugin","version":"?"}` | Instalado via `npm install` |

Quando `ref` e `sha` estão ambos definidos, o `sha` é o pin efetivo.

---

## 6. Frontmatter de SKILL.md

```yaml
---
name: minha-skill
description: <verbo + objeto + resultado>. Use quando <contextos>. Não use para <casos vizinhos>.
disable-model-invocation: false
user-invocable: true
allowed-tools:
  - Read
  - Glob
  - Grep
disallowed-tools:
  - Bash
---
```

| Campo | Efeito |
|---|---|
| `name` | Identificador; kebab-case |
| `description` | **Mecanismo primário de ativação.** Toda informação de "quando usar" mora aqui, não no corpo |
| `disable-model-invocation: true` | A skill só roda quando chamada manualmente |
| `user-invocable: false` | Não aparece no menu `/`; serve como conhecimento auxiliar |
| `allowed-tools` | Pré-aprova o mínimo necessário. Não é autorização ampla de negócio |
| `disallowed-tools` | Proíbe ferramenta que contradiz a responsabilidade da skill |

Argumentos do usuário chegam por `$ARGUMENTS`, `$ARGUMENTS[N]` ou `$N`.

**Nota de compatibilidade:** a documentação oficial mostra exemplos de SKILL.md com apenas `description` no frontmatter. `name` é aceito e recomendado para plugins de portfólio, porque torna o arquivo autoexplicativo. Confirme na Fase 0 se algum campo passou a ser rejeitado.

---

## 7. Frontmatter de agente

```yaml
---
name: nome-do-agente
description: <especialidade, gatilhos e resultado esperado>
tools: Read, Glob, Grep
model: sonnet
---
```

Não presuma que campos de permissão, hooks ou MCP declarados no frontmatter de um agente empacotado em plugin serão aplicados. Teste se o agente aparece e se pode ser chamado pelo nome qualificado.

Evite agentes que apenas renomeiam uma skill sem ganhar isolamento de contexto ou especialização real.

---

## 8. hooks.json

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}/scripts/validate-changed-file.sh\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

Regras: trate stdin como entrada não confiável; use parsing seguro em vez de interpolação direta em shell; documente evento, matcher, efeito, timeout e falha esperada; explique como diagnosticar e desabilitar caso o hook bloqueie trabalho.

**Um `hooks/hooks.json` malformado impede o plugin inteiro de carregar.** Valide o JSON sempre.

---

## 9. Variáveis de ambiente

| Variável | Uso correto |
|---|---|
| `${CLAUDE_PLUGIN_ROOT}` | Localizar arquivos empacotados com o plugin |
| `${CLAUDE_PLUGIN_DATA}` | Estado persistente que deve sobreviver a atualizações |
| `${CLAUDE_PROJECT_DIR}` | Recursos pertencentes ao projeto do usuário |

Nunca dependa do diretório corrente implícito. Scripts devem funcionar a partir de caminhos resolvidos.

---

## 10. Nomes reservados de marketplace

Estes nomes são reservados para uso oficial da Anthropic e **fazem o marketplace parar de carregar** se usados por terceiros:

```
claude-code-marketplace       claude-code-plugins
claude-plugins-official       claude-plugins-community
claude-community              anthropic-marketplace
anthropic-plugins             agent-skills
anthropic-agent-skills        knowledge-work-plugins
life-sciences                 claude-for-legal
claude-for-financial-services financial-services-plugins
first-party-plugins           healthcare
```

Nomes que **imitam** fontes oficiais também são bloqueados — por exemplo `official-claude-plugins`, `anthropic-plugins-v2`.

A verificação roda a cada carregamento, não só na adição. Um marketplace registrado antes de um nome virar reservado para de funcionar e reporta origem não confiável.

**Consequência prática:** escolha um nome pessoal e inequívoco. `<seu-usuario>-plugins` ou `<sua-marca>-tools` são seguros. Confirme a lista na Fase 0, porque ela cresce.
