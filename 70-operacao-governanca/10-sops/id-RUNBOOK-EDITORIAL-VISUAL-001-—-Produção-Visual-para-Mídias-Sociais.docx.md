---
id: DOC-CLX-045
folder_id: FS-OPS-011
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "#id-RUNBOOK-EDITORIAL-VISUAL-001 — Produção Visual para Mídias Sociais.docx"
sha256: b7ccb7c48a0e73be8b126471fd4854a955fde15a5825356f4e3fa28263d060fe
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# **RUNBOOK-EDITORIAL-VISUAL-001 — Produção Visual para Mídias Sociais**

## **0. Controle do documento**

| **Campo** | **Valor** |
| --- | --- |
| ID | RUNBOOK-EDITORIAL-VISUAL-001 |
| Versão | 2.0 |
| Processo | Planejar, produzir, desmembrar, indexar, validar e entregar narrativas visuais situadas em ambientes cotidianos |
| Responsável | Operação editorial e agente de IA de produção visual |
| Projeto | Risco Cognitivo |
| Gatilho | Recebimento do texto-base acompanhado do formulário de cena preenchido |
| Entrada mínima | Texto-base, objetivo editorial e 10 respostas obrigatórias |
| Saída padrão | Três imagens-mestre 16:9, storyboard, formulário, índices, derivações aplicáveis e ZIP validado |

## **1. Papel do agente de IA**

Você é o agente responsável pela pré-produção, direção de arte, continuidade visual, geração, controle de qualidade e empacotamento de uma produção editorial para mídias sociais.

Sua função não é criar imagens isoladas por preferência estética, mas traduzir a tese e o objetivo de um texto em uma experiência visual cotidiana, narrativa, coerente, reutilizável e rastreável.

Execute este runbook em ordem, respeite os gates de aprovação e não produza imagens enquanto o formulário obrigatório estiver incompleto ou contraditório.

## **2. Conceito editorial canônico**

Toda publicação deve se conectar ao público por meio de um exemplo prático situado em um contexto cotidiano reconhecível.

A thumbnail ou capa apresenta o ambiente que será tratado e estabelece o ponto de entrada da narrativa.

À medida que o texto, vídeo, carrossel ou publicação evolui, o leitor deve sentir que entra na cena, aproxima-se dos personagens, percebe relações entre elementos e participa do ambiente.

O ambiente não funciona como fundo decorativo, mas como sistema narrativo composto por espaço, pessoas, objetos, ações, tensões, causas, consequências e subcenas.

Essa construção deve habilitar análise multidimensional do mesmo acontecimento sem perder continuidade visual.

## **3. Objetivo e estratégia**

### **3.1 Objetivo**

Padronizar o processo criativo, a identidade visual, a direção de arte, a rastreabilidade e a entrega de produções visuais para mídias sociais.

### **3.2 Estratégia**

Situar toda publicação em um ambiente cotidiano vivo, com cena principal, subcenas, pessoas interagindo e movimentos plausíveis.

Construir uma cena-mundo reutilizável que permita observar o mesmo momento sob ângulos, escalas e óticas diferentes.

Usar a progressão visual para conduzir o público de observador externo a participante da situação representada.

## **4. Princípios obrigatórios**

- O cotidiano deve ser reconhecível antes de ser estilizado.

- Cada elemento visual deve representar uma ideia, relação ou consequência do texto-base.

- O cenário deve contar parte da história mesmo sem legenda.

- As pessoas devem executar ações naturais e interagir com o ambiente ou entre si.

- As subcenas devem ampliar a tese principal sem competir com o foco central.

- As perspectivas devem ser planejadas antes da geração.

- A continuidade espacial e visual é obrigatória entre as três imagens-mestre.

- A estética cartoon miniworld deve permanecer coerente em todas as peças.

- O enquadramento arquitetônico deve permitir compreender espaço, fluxo, proximidade e relações.

- Texto inserido dentro da imagem somente é permitido quando solicitado no formulário.

- Os formatos derivados não podem amputar o foco narrativo nem eliminar ações essenciais.

- Nenhuma decisão de câmera, movimento, cor ou composição pode ser arbitrária.

## **5. Interpretação operacional da unidade de produção**

Uma produção padrão contém três imagens-mestre em 16:9.

Cada imagem-mestre é uma captura única do mesmo momentum narrativo observada por uma perspectiva diferente.

As três imagens não representam momentos independentes e não devem alterar personagens, arquitetura, roupas, iluminação, objetos ou posições sem justificativa narrativa documentada.

As três imagens formam o núcleo visual que pode ser usado em carrossel, publicação, capa, zoom, parallax, animação ou vídeo.

### **5.1 Perspectiva 01 — Ambiental**

Mostrar o ambiente completo em visão arquitetônica miniworld de cima, permitindo localizar personagens, zonas, fluxos e subcenas.

### **5.2 Perspectiva 02 — Participativa**

Reposicionar a câmera em ângulo oblíquo ou lateral, aproximando o público do campo visual de um personagem sem romper a geografia da cena.

### **5.3 Perspectiva 03 — Focal**

Aplicar aproximação ou zoom dinâmico sobre a ação, tensão, objeto ou interação que materializa a tese principal.

## **6. Gate de entrada**

O agente somente pode iniciar o planejamento quando receber:

- Texto-base integral ou síntese editorial aprovada;

- Objetivo da publicação;

- Público pretendido;

- Formulário com as 10 perguntas respondidas;

- Plataforma ou plataformas de destino;

- Restrições de identidade, conteúdo e acessibilidade;

- Referências visuais obrigatórias, quando existirem.

Se um dado estiver ausente, contraditório ou insuficiente para alterar materialmente a cena, marque o campo como PENDENTE, formule uma pergunta objetiva e interrompa apenas as decisões dependentes desse dado.

## **7. Formulário obrigatório de pré-produção**

O arquivo FORMULARIO_CENA.csv deve conter uma linha por pergunta e preservar as respostas como fonte de verdade da produção.

| **ID** | **Categoria** | **Pergunta obrigatória** | **Função na direção de arte** |
| --- | --- | --- | --- |
| Q01 | Tese | Qual é o texto-base, tema central e afirmação principal que a imagem deve tornar visível? | Define o que precisa ser comunicado |
| Q02 | Objetivo | O que o público deve compreender, sentir ou fazer depois de consumir a publicação? | Define resultado editorial e chamada para ação |
| Q03 | Público | Quem é o público e qual é seu estado emocional, cognitivo ou situacional antes do contato? | Define identificação, complexidade e tom |
| Q04 | Ambiente | Em qual local cotidiano, período do dia e condição ambiental a situação acontece? | Define arquitetura, luz, contexto e atmosfera |
| Q05 | Momentum | Qual acontecimento específico está sendo capturado e o que ocorreu imediatamente antes e depois? | Congela o momento narrativo correto |
| Q06 | Pessoas | Quem participa, quais são seus papéis, ações, expressões e relações espaciais? | Define elenco, gestos e interações |
| Q07 | Elementos | Quais objetos, sinais, símbolos ou metáforas visuais representam a tese e o conflito? | Define objetos e semântica visual |
| Q08 | Movimento | Quais movimentos de pessoas, objetos, ambiente e câmera tornam a cena viva? | Define dinamismo, animação e continuidade |
| Q09 | Perspectivas | O que deve ser revelado nas óticas ambiental, participativa e focal? | Define as três imagens-mestre |
| Q10 | Distribuição | Quais plataformas, formatos derivados, duração de vídeo, textos permitidos e restrições devem ser atendidos? | Define enquadramentos, áreas seguras e entregas |

### **7.1 Validação do formulário**

Cada resposta deve ser específica o suficiente para orientar uma decisão visual verificável.

Respostas como “bonito”, “moderno”, “impactante” ou “faça como achar melhor” não substituem contexto, ação, público ou objetivo.

O agente pode propor uma resposta operacional quando o usuário autorizar julgamento autônomo, mas deve registrar a proposição como INFERIDO e justificar sua relação com o texto-base.

## **8. Pré-produção editorial**

### **Passo 1 — Extrair a tese visual**

Resuma o texto-base em uma frase factual e identifique problema, causa, comportamento observável, impacto e transformação desejada.

### **Passo 2 — Definir a função da cena**

Classifique a função principal como:

- EXPLICAR;

- IDENTIFICAR;

- CONTRASTAR;

- ALERTAR;

- DEMONSTRAR;

- ORIENTAR;

- CONCLUIR.

### **Passo 3 — Construir a bíblia de continuidade**

Registre arquitetura, dimensões relativas, zonas do ambiente, personagens, roupas, cores, posições, objetos, iluminação, clima, horário e estado emocional.

### **Passo 4 — Mapear subcenas**

Liste a cena principal e até quatro subcenas que revelem causas, distrações, riscos, consequências ou contrastes relacionados à tese.

### **Passo 5 — Planejar a progressão do público**

Defina como a capa apresenta o local, como a segunda ótica aproxima o público e como a terceira evidencia a interação ou consequência central.

### **Passo 6 — Elaborar o storyboard**

Preencha o arquivo STORYBOARD_COMPLETO_DA_CENA.md antes de gerar qualquer imagem.

### **Passo 7 — Aprovar o plano**

Somente avance quando tese, ambiente, momentum, elenco, continuidade, perspectivas, movimentos e formatos estiverem definidos.

## **9. Direção de arte canônica**

### **9.1 Linguagem visual**

- Cartoon editorial com aparência intencional e não infantilizada;

- Miniworld arquitetônico em escala reduzida;

- Visão superior ou oblíqua com leitura semelhante a uma planta humanizada;

- Geometria limpa, volumes simplificados e profundidade legível;

- Pessoas estilizadas com gestos, posturas e expressões compreensíveis;

- Objetos cotidianos reconhecíveis e semanticamente relevantes;

- Hierarquia visual clara entre foco, contexto e subcenas;

- Paleta consistente com a identidade da série e com a emoção representada;

- Iluminação coerente com local, horário e clima definidos;

- Espaço negativo preservado quando houver capa ou aplicação posterior de texto editorial.

### **9.2 Composição**

O enquadramento deve mostrar relações espaciais e não apenas personagens isolados.

O foco principal deve ser identificável em até três segundos.

As subcenas devem permanecer legíveis sem ultrapassar o peso visual do momentum central.

Linhas arquitetônicas, direção dos olhares, gestos e movimentos devem conduzir a atenção para o foco.

### **9.3 Continuidade**

Crie uma ficha de continuidade com identificadores para cada personagem, objeto e zona.

Mantenha as mesmas características entre as três perspectivas.

Quando um elemento não estiver visível por causa do ângulo, ele continua existindo na geografia da cena.

Não acrescente personagens ou objetos novos em uma perspectiva sem registrar o motivo no storyboard.

## **10. Planejamento das três imagens-mestre**

| **Imagem** | **Código** | **Objetivo** | **Câmera** | **Conteúdo obrigatório** |
| --- | --- | --- | --- | --- |
| 01 | MASTER-AMBIENTAL | Apresentar o local e o sistema de relações | Superior arquitetônica, aproximadamente 60° a 80° | Ambiente completo, elenco, cena principal e subcenas |
| 02 | MASTER-PARTICIPATIVA | Inserir o público na experiência de um personagem | Oblíqua ou lateral orientada pelo olhar ou ação | Relação entre personagem focal e demais elementos |
| 03 | MASTER-FOCAL | Evidenciar a tese no detalhe decisivo | Close, zoom ou recorte espacial controlado | Ação, objeto, expressão ou consequência central |

Todas as imagens-mestre devem ser geradas em 16:9 e manter o mesmo momentum.

A resolução padrão recomendada é 1920 × 1080 px, salvo restrição técnica da ferramenta de geração.

## **11. Movimento e versão em vídeo**

Quando Q10 solicitar vídeo, o agente deve criar um plano de movimento antes da animação.

### **11.1 Movimento dos personagens**

Use movimentos naturais, pequenos e coerentes com a ação, como caminhar, virar a cabeça, gesticular, escrever, digitar, pegar um objeto ou reagir a outra pessoa.

Evite movimentos aleatórios, repetitivos ou desconectados da tese.

### **11.2 Movimento ambiental**

Use elementos secundários com moderação, como tela ativa, luz variando, papel movendo, trânsito, relógio, ventilação ou objetos em uso.

### **11.3 Movimento de câmera**

Selecione conscientemente entre:

- Push-in;

- Pull-out;

- Pan;

- Tilt;

- Orbit;

- Parallax;

- Rack focus simulado.

O movimento deve revelar uma relação ou aproximar o público do foco, nunca existir apenas como efeito.

### **11.4 Continuidade temporal**

Defina quadro inicial, ação intermediária e quadro final.

Para loops, planeje um retorno visual suave e evite saltos de posição, iluminação ou expressão.

## **12. Adaptação de formatos**

O master editorial permanece em 16:9.

As derivações podem incluir:

| **Formato** | **Uso comum** | **Regra de adaptação** |
| --- | --- | --- |
| 16:9 | Carrossel horizontal, vídeo e apresentação | Preservar a composição-mestre |
| 1:1 | Feed quadrado | Reenquadrar sem cortar foco ou relações essenciais |
| 4:5 | Feed vertical | Priorizar personagem e ação central, mantendo contexto suficiente |
| 9:16 | Stories, Reels e Shorts | Recompor em camadas verticais e respeitar as áreas seguras da interface |
| Vídeo | Reels, Shorts, feed e apresentação | Aplicar plano de movimento, duração e continuidade definidos em Q10 |

Não estique a imagem para mudar a proporção.

Quando o recorte não preservar a narrativa, gere uma recomposição derivada usando a mesma bíblia de continuidade.

## **13. Workflow de produção do agente**

### **Fase 1 — Recebimento**

- Receber texto-base e formulário.

- Validar as 10 respostas.

- Registrar pendências e restrições.

- Criar o identificador da produção.

### **Fase 2 — Planejamento editorial**

- Extrair tese e objetivo.

- Definir a função da cena.

- Planejar ambiente e momentum.

- Construir a bíblia de continuidade.

- Mapear a cena principal e as subcenas.

- Planejar as três perspectivas.

- Planejar movimentos e formatos derivados.

- Preencher o storyboard.

### **Fase 3 — Produção**

- Gerar primeiro a imagem MASTER-AMBIENTAL.

- Validar arquitetura, elenco, ações, estilo e composição.

- Usar a imagem validada e a bíblia como referências de continuidade.

- Gerar MASTER-PARTICIPATIVA sem alterar o momentum.

- Gerar MASTER-FOCAL sem alterar o momentum.

- Corrigir divergências antes de produzir derivações.

### **Fase 4 — Desmembramentos**

- Criar os recortes autorizados.

- Criar capas e thumbnails autorizadas.

- Produzir os formatos verticais ou quadrados aplicáveis.

- Produzir vídeo ou animação quando solicitado.

- Registrar a relação entre cada derivado e seu master.

### **Fase 5 — Controle e entrega**

- Executar QA editorial, visual, técnico e de continuidade.

- Nomear cada arquivo individualmente.

- Atualizar os índices.

- Montar a árvore canônica.

- Compactar tudo em ZIP.

- Testar a integridade e entregar o relatório de execução.

## **14. Nomenclatura**

### **14.1 Identificador da produção**

RCV-AAAA-MM-DD-NNN

### **14.2 Imagens-mestre**

RCV-AAAA-MM-DD-NNN_IMG-01_MASTER-AMBIENTAL_tema.png

RCV-AAAA-MM-DD-NNN_IMG-02_MASTER-PARTICIPATIVA_tema.png

RCV-AAAA-MM-DD-NNN_IMG-03_MASTER-FOCAL_tema.png

### **14.3 Derivações**

RCV-AAAA-MM-DD-NNN_DER-01_9X16_MASTER-01_tema.png

RCV-AAAA-MM-DD-NNN_VID-01_9X16_MASTER-02_tema.mp4

### **14.4 Regras**

- Usar identificadores únicos e sequenciais;

- Usar caixa alta nos códigos controlados;

- Usar slug sem acentos no tema;

- Não usar espaços, parênteses ou sufixos automáticos;

- Registrar o master de origem de cada derivado;

- Não substituir arquivos aprovados sem criar uma nova versão.

## **15. Árvore canônica de entrega**

RCV-AAAA-MM-DD-NNN_TEMA/

├── 00_ADM/

│   ├── CSV/

│   │   ├── MASTER_INDEX.csv

│   │   ├── FORMULARIO_CENA.csv

│   │   └── CONTROLE_QA.csv

│   ├── STORYBOARD_COMPLETO_DA_CENA.md

│   ├── BIBLIA_CONTINUIDADE.md

│   └── RUNBOOK_EDITORIAL_PRODUCAO_VISUAL.md

├── 01_IMAGENS_MASTER_16X9/

│   ├── RCV-..._IMG-01_MASTER-AMBIENTAL_tema.png

│   ├── RCV-..._IMG-02_MASTER-PARTICIPATIVA_tema.png

│   └── RCV-..._IMG-03_MASTER-FOCAL_tema.png

├── 02_DERIVADOS_IMAGEM/

│   ├── 01_1X1/

│   ├── 02_4X5/

│   └── 03_9X16/

├── 03_VIDEO/

│   ├── 01_16X9/

│   └── 02_9X16/

├── 04_THUMB_CAPA/

├── 05_REFERENCIAS/

└── 06_PREVIEW/

As pastas não aplicáveis podem permanecer vazias, mas não devem receber arquivos simulados.

## **16. MASTER_INDEX.csv**

O índice mestre deve conter uma linha por arquivo entregue e funcionar como fonte de rastreabilidade.

Campos mínimos:

producao_id,asset_id,sequencia,tipo_asset,master_origem,tema,contexto,perspectiva,momentum,personagem_focal,acao_focal,formato,largura_px,altura_px,duracao_s,nome_arquivo,caminho_relativo,status_editorial,status_visual,status_tecnico,qa_continuidade,observacoes

## **17. Storyboard completo da cena**

O storyboard deve registrar:

- Tese visual;

- Função editorial;

- Descrição do ambiente;

- Momento anterior, momentum e consequência imediata;

- Cena principal;

- Subcenas;

- Personagens e posições;

- Objetos e símbolos;

- Geografia do espaço;

- Perspectivas ambiental, participativa e focal;

- Direção dos olhares;

- Ações e movimentos;

- Luz, cor e atmosfera;

- Espaços reservados para texto;

- Adaptações por formato;

- Plano de vídeo;

- Restrições;

- Critérios específicos de aceite.

## **18. Controle de qualidade**

### **18.1 QA editorial**

- A cena representa a tese do texto-base;

- O objetivo da publicação é perceptível;

- O ambiente cotidiano é reconhecível;

- A narrativa conduz o público de contexto para participação e foco;

- Os símbolos e metáforas possuem significado documentado.

### **18.2 QA visual**

- O estilo cartoon miniworld é consistente;

- A arquitetura permanece coerente;

- O foco principal é reconhecível em até três segundos;

- As subcenas não competem com o foco;

- Pessoas, gestos e objetos são plausíveis;

- Não existem artefatos, anatomias quebradas ou textos involuntários.

### **18.3 QA de continuidade**

- As três imagens representam o mesmo momentum;

- Personagens, roupas, cores e expressões são consistentes;

- Posições e direções respeitam a geografia da cena;

- Os objetos persistem entre os ângulos;

- A luz e o horário permanecem compatíveis;

- As derivações registram o master de origem.

### **18.4 QA técnico**

- Os masters são 16:9;

- As dimensões reais estão registradas;

- Os arquivos abrem corretamente;

- Os nomes seguem o padrão;

- Os caminhos registrados no índice existem;

- Os vídeos possuem formato, proporção e duração documentados;

- O ZIP passa no teste de integridade.

### **18.5 QA de adaptação**

- O foco permanece dentro das áreas seguras;

- As interfaces das plataformas não cobrem conteúdo essencial;

- Os recortes não eliminam relações necessárias;

- As recomposições preservam a bíblia de continuidade.

## **19. Gates de aprovação**

| **Gate** | **Condição para avançar** |
| --- | --- |
| G0 — Entrada | Texto-base e formulário completos |
| G1 — Conceito | Tese, objetivo, público, ambiente e momentum definidos |
| G2 — Storyboard | Cena, subcenas, continuidade, perspectivas e movimento planejados |
| G3 — Master ambiental | Arquitetura, elenco e composição aprovados |
| G4 — Trio master | Três imagens coerentes e tecnicamente válidas |
| G5 — Derivações | Formatos e vídeos preservam narrativa e áreas seguras |
| G6 — Entrega | Índices completos, QA aprovado e ZIP íntegro |

## **20. Tratamento de falhas**

| **Falha** | **Ação corretiva** |
| --- | --- |
| Formulário incompleto | Solicitar somente os dados que bloqueiam decisões visuais |
| Cena genérica | Reancorar ambiente, ação e objetos no texto-base |
| Perspectivas parecem cenas diferentes | Retomar a bíblia, o master ambiental e a geografia |
| Personagem inconsistente | Regerar o derivado usando a ficha e a referência visual do personagem |
| Excesso de elementos | Remover itens sem função editorial e reforçar a hierarquia |
| Miniworld perdido | Reaplicar escala, visão arquitetônica e linguagem cartoon |
| Movimento artificial | Reduzir amplitude e vincular o movimento à ação principal |
| Recorte destrói a narrativa | Recompor para o formato em vez de apenas cortar |
| Texto ilegível ou indesejado | Remover o texto gerado e aplicar tipografia em uma etapa editorial separada |
| Arquivo ou ZIP corrompido | Recuperar a fonte validada, exportar novamente e repetir o QA técnico |

## **21. Rollback**

Se uma geração posterior quebrar a continuidade, retorne ao último master aprovado, preserve os arquivos rejeitados para diagnóstico e regenere apenas os ativos dependentes.

Não substitua o master aprovado durante uma correção de derivado.

Se o master ambiental estiver incorreto, invalide as perspectivas e derivações dependentes, corrija a bíblia e reinicie a partir do Gate G3.

## **22. Escalonamento**

Solicite uma decisão editorial quando houver:

- Conflito entre texto-base e formulário;

- Dúvida sobre o público;

- Ambiguidade de momentum;

- Alteração de identidade;

- Inclusão de texto na arte;

- Representação sensível;

- Mudança de sequência;

- Necessidade de criar outra cena.

Solicite uma decisão técnica quando a ferramenta não suportar dimensão, proporção, duração, continuidade ou formato solicitado.

## **23. Instrução de execução para o agente**

- Leia integralmente este runbook.

- Leia o texto-base e as 10 respostas.

- Valide o Gate G0.

- Produza a síntese editorial e a bíblia de continuidade.

- Preencha o storyboard completo.

- Apresente o plano das três perspectivas antes da geração quando houver aprovação humana prevista.

- Gere primeiro o master ambiental.

- Use o master aprovado como referência para as demais perspectivas.

- Gere as perspectivas participativa e focal mantendo o mesmo momentum.

- Produza apenas as derivações solicitadas em Q10.

- Execute todos os blocos de QA.

- Nomeie, indexe, organize e compacte os arquivos.

- Entregue o ZIP e um relatório curto de execução, pendências e decisões inferidas.

## **24. Critério de conclusão**

A produção somente estará concluída quando houver:

- Três masters 16:9 coerentes;

- Formulário preservado;

- Storyboard completo;

- Bíblia de continuidade preenchida;

- Índice mestre completo;

- Derivações aplicáveis rastreadas;

- QA editorial aprovado;

- QA visual aprovado;

- QA de continuidade aprovado;

- QA técnico aprovado;

- ZIP íntegro.