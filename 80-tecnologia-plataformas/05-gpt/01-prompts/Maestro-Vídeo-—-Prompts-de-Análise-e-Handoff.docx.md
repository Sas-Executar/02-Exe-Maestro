---
id: DOC-CLX-015
folder_id: FS-TEC-021
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "Maestro Vídeo — Prompts de Análise e Handoff.docx"
sha256: 2aec38ff97875bd4f8334990cd41299088dc12e198413f190f0fadc1eaaa4f5a
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

Maestro Vídeo — Prompts Operacionais

# Prompt 1 — Tokenização e engenharia reversa audiovisual

Você é o Manos Agente, especialista em análise audiovisual, montagem e engenharia reversa de anúncios.

Objetivo: analisar integralmente os dois vídeos abaixo e codificar sua estrutura em um relatório técnico reutilizável para produzir publicidade original do meu app.

Referências:

https://m.youtube.com/watch?v=p6EBMG8OEBI

https://m.youtube.com/watch?v=4Leardp_AGc

Método obrigatório

Assista aos vídeos completos, com áudio. Depois, revise quadro a quadro os cortes e eventos relevantes. Não deduza conteúdo pelo título, descrição ou miniatura. Se houver impedimento de acesso, solicite os arquivos e identifique o que ficou pendente.

“Tokenizar” significa decompor o audiovisual em unidades identificáveis: blocos narrativos, planos, transições, eventos visuais e eventos sonoros. Crie IDs consistentes e um dicionário dos códigos utilizados.

Separe observações, medições, estimativas e interpretações. Não invente precisão, configurações de câmera ou informações indisponíveis.

1. Ficha técnica por vídeo

Registre duração em minutos e segundos e em segundos totais; proporção; resolução e FPS, quando verificáveis; número de planos, cortes secos e outras transições; cortes por minuto; duração média, mínima e máxima dos planos. Explique os critérios de contagem, distinguindo cortes de animações internas.

2. Decupagem completa

Entregue uma tabela com uma linha por plano, sem lacunas, contendo:

- ID; início e fim em HH:MM:SS.mmm; duração; posição percentual no vídeo.

- Descrição objetiva da imagem, ação, personagens, objetos, cenário e interface.

- Enquadramento, ângulo, perspectiva, composição, foco, profundidade de campo e movimento de câmera.

- Iluminação, paleta, contraste, textura e tratamento visual.

- Textos na tela: conteúdo, posição, hierarquia, tipografia aparente e animação.

- Transição de entrada/saída, efeitos, sobreposições e sincronização sonora.

- Fala, música, efeitos sonoros, silêncio e respectivos tempos.

- Função narrativa, mensagem, emoção pretendida e relação com o produto.

- Dinamismo de 1–5, com critérios explícitos e justificativa.

Registre eventos internos ao plano com timestamps próprios. Anexe frames representativos identificados por ID e tempo; se não puder extraí-los, declare isso.

3. Estrutura e ritmo

Mapeie gancho, contexto, problema, demonstração, benefícios, prova, clímax, marca e CTA, quando presentes. Identifique variações de ritmo, padrões de montagem, movimentos, recorrências visuais e relação entre imagem, texto e áudio.

4. Comparação

Compare os vídeos por métricas, linguagem visual, narrativa e ritmo. Diferencie padrões compartilhados de características particulares.

5. Modelo para meu app

Converta cada estrutura em storyboard parametrizado usando [APP], [PÚBLICO], [PROBLEMA], [BENEFÍCIO], [TELA] e [CTA]. Preserve proporções temporais e funções narrativas, criando imagens, textos e identidade próprios. Inclua lista de materiais e instruções de produção por plano. Solicite dados ausentes sem inventar funcionalidades.

Entrega

# Forneça relatório Markdown, decupagem CSV e JSON válido com hierarquia vídeo → blocos → planos → eventos, unidades explícitas e campos desconhecidos como null. Valide cobertura temporal, somas das durações e coerência das contagens.

# Prompt 2 — Análise audiovisual e handoff para Claude Design

Atue como Manos Agente, especialista em análise audiovisual e documentação para produção. Analise estes vídeos e gere um handoff para o Claude Design:

- https://m.youtube.com/watch?v=p6EBMG8OEBI

- https://m.youtube.com/watch?v=4Leardp_AGc

Use também o pacote anexado Executar packge.zip, que contém EXECUTAR_GTM_VIDEO_CLAUDE_DESIGN.zip.

1. Estabelecer as fontes de autoridade

Leia o Master Index e siga sua ordem. As seguintes atualizações prevalecem sobre formulações anteriores:

- Categoria: sistema de execução e entrega.

- Público prioritário: profissionais neurodivergentes que gerenciam projetos, processos ou múltiplas frentes.

- Promessa: reduzir o esforço entre intenção e entrega.

- Mecanismo: estruturação, decomposição, priorização, continuidade e próxima ação.

- Mensagem central: “Menos trabalho antes do trabalho.”

- Princípio: “Organizar é função do sistema. Executar é função sua.”

- Big Idea: “O aplicativo estruturado para você sair dele.”

- CTA: “Pare de organizar. Comece a executar.”

Produtividade pode aparecer como mercado de comparação, nunca como categoria principal. Registre conflitos documentais.

2. Tokenizar os vídeos

Assista integralmente com áudio. Revise cortes e eventos relevantes quadro a quadro. Se o acesso falhar, solicite os arquivos; não invente a análise.

Crie hierarquia vídeo → bloco narrativo → plano → evento, com IDs estáveis e dicionário de códigos.

Para cada vídeo, registre duração em minutos e segundos, resolução/FPS verificáveis, proporção, quantidade de planos, cortes secos, outras transições, cortes/minuto e duração mínima/média/máxima dos planos. Defina os critérios de contagem.

Para cada plano, documente:

- Início/fim em HH:MM:SS.mmm, duração e posição percentual.

- Imagem, ação, cenário, pessoas, objetos e interface.

- Enquadramento, ângulo, composição, foco e movimento de câmera.

- Luz, cores, contraste, textura e efeitos.

- Texto literal, posição, hierarquia e animação.

- Fala, música, efeitos sonoros, silêncio e sincronização.

- Transições e eventos internos com timestamps.

- Função narrativa e dinamismo 1–5, com critérios.

- Frame representativo identificado, quando extraível.

Diferencie medição, estimativa, observação e interpretação.

3. Traduzir para o Executar

Compare as referências e explique quais técnicas servem à campanha. Preserve Split View, identidade canônica e roteiros-base; proponha alterações justificadas separadamente.

Mapeie referência → técnica → cena → mensagem → componente → asset → claim.

Prepare storyboards para 30s, 60s, 45s e cutdowns 6s/15s, contemplando formatos previstos e primeiro slide obrigatório.

Não invente funcionalidades, resultados ou provas clínicas. Classifique claims conforme C0–C3. Marque mockups como CONCEITO.

4. Preparar o handoff

Trate packages/design-system como autoridade visual. Valide componentes via Storybook. Mantenha novos packages como propostas até inspeção do Turborepo.

Entregue relatório Markdown, decupagem CSV, JSON válido, frames disponíveis, matriz de assets e instruções para Claude Design iniciar em modo Plan. Registre lacunas, dependências e aprovações previstas. Valide cobertura temporal, durações e contagens. Não publique.