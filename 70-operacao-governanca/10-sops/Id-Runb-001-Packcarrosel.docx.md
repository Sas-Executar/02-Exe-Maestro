---
id: DOC-CLX-044
folder_id: FS-OPS-011
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "#Id-Runb-001-Packcarrosel.docx"
sha256: 152795f3a10db52306aea654529c556a12c2856f4511f246824befd33ff181ba
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# **RUNBOOK-IMG-001 — Organização de Pack de Carrossel por Contexto**

## **1. Controle do documento**

| **Campo** | **Valor** |
| --- | --- |
| ID | RUNBOOK-IMG-001 |
| Processo | Organizar, nomear, indexar, validar e compactar packs de imagens |
| Versão | 1.0 |
| Responsável | Operação editorial do projeto Risco Cognitivo |
| Gatilho | Recebimento de imagens individuais ou de um ZIP com peças aprovadas |
| Saída | Diretório único organizado, MASTER_INDEX.csv e pacote ZIP validado |

## **2. Objetivo**

Padronizar a entrega de packs editoriais para que cada imagem possua identificação única, contexto explícito, caminho rastreável e validação antes da distribuição.

## **3. O que aconteceu nesta execução**

O pacote original com 15 arquivos PNG foi localizado, extraído e reorganizado em quatro contextos: Trabalho, Aprendizagem, Vida Pessoal e Encerramento.

Cada arquivo recebeu um ID sequencial de SC-001 a SC-015, um tema em caixa alta e um título descritivo em formato slug.

Foi criado o arquivo MASTER_INDEX.csv com sequência, contexto, tema, título, nome, caminho relativo, formato, dimensão real e status.

As imagens foram preservadas sem alteração visual.

As dimensões originais, próximas de 3:1, foram registradas no índice em vez de serem declaradas incorretamente como 16:9.

O diretório foi compactado em um único ZIP e submetido a testes de integridade e conferência de quantidade.

## **4. Estrutura canônica**

PACOTE_SOBRECARGA_COGNITIVA_15/

├── MASTER_INDEX.csv

├── RUNBOOK_ORGANIZACAO_PACK_CARROSSEL.md

├── 01_TRABALHO/

├── 02_APRENDIZAGEM/

├── 03_VIDA_PESSOAL/

└── 04_ENCERRAMENTO/

## **5. Regra de classificação**

| **Contexto** | **Conteúdo aceito** |
| --- | --- |
| 01_TRABALHO | Trabalho, escritório, reuniões e rotinas profissionais |
| 02_APRENDIZAGEM | Escola, faculdade, estudos e formação |
| 03_VIDA_PESSOAL | Casa, trânsito, digital, decisões, finanças, relacionamentos, lazer e saúde mental |
| 04_ENCERRAMENTO | Síntese, chamada para ação, conclusão ou fechamento narrativo |

## **6. Convenção de nomes**

Aplicar obrigatoriamente o seguinte padrão:

SC-NNN_TEMA_titulo-descritivo.png

Regras:

- SC identifica a série Sobrecarga Cognitiva.

- NNN representa a ordem narrativa com três dígitos.

- TEMA deve ser escrito em caixa alta e sem acentos.

- Termos compostos do tema devem utilizar hífen.

- O título descritivo deve ser escrito em letras minúsculas.

- Remover acentos do título descritivo.

- Separar as palavras do título com hífen.

- Não utilizar espaços nos nomes dos arquivos.

- Não utilizar parênteses ou caracteres especiais.

- Não manter duplicadores automáticos como (1), (2) ou cópia.

Exemplo:

SC-006_ESCRITORIO_sobrecarga-cognitiva-no-escritorio.png

## **7. Procedimento operacional**

### **Passo 1 — Receber e preservar a origem**

Copie o pacote recebido para uma área temporária de trabalho.

Mantenha o arquivo original intacto durante todo o procedimento para permitir recuperação ou rollback.

Não edite, renomeie ou substitua diretamente os arquivos originais.

### **Passo 2 — Inventariar**

Liste todos os arquivos recebidos.

Para cada arquivo, verifique:

- Nome original;

- Formato;

- Dimensões em pixels;

- Tamanho;

- Legibilidade;

- Existência de duplicidades;

- Existência de corrupção;

- Ordem narrativa aparente.

Registre divergências antes de continuar.

### **Passo 3 — Classificar por contexto**

Associe cada imagem a somente um contexto canônico:

- Trabalho;

- Aprendizagem;

- Vida Pessoal;

- Encerramento.

Utilize o objetivo editorial principal da peça para decidir sua classificação.

Não duplique a mesma imagem em várias pastas apenas porque ela pode se relacionar com mais de um contexto.

Encaminhe casos ambíguos para decisão editorial.

### **Passo 4 — Nomear individualmente**

Aplique a convenção:

SC-NNN_TEMA_titulo-descritivo.png

Preserve a ordem narrativa original.

Utilize IDs sequenciais e exclusivos.

Não altere a imagem durante a renomeação.

### **Passo 5 — Criar o índice mestre**

Crie um arquivo chamado:

MASTER_INDEX.csv

Registre exatamente uma linha para cada imagem.

O CSV deve conter os seguintes campos:

item_id,sequencia,contexto,tema,titulo,nome_arquivo,caminho_relativo,formato,proporcao,status

Definição dos campos:

| **Campo** | **Regra** |
| --- | --- |
| item_id | Identificador único no padrão SC-NNN |
| sequencia | Posição narrativa da peça |
| contexto | Grupo contextual principal |
| tema | Assunto específico da imagem |
| titulo | Título editorial legível |
| nome_arquivo | Nome padronizado do PNG |
| caminho_relativo | Caminho do arquivo dentro do pacote |
| formato | Formato real do arquivo |
| proporcao | Dimensões reais em pixels |
| status | Estado de validação da peça |

Não invente dimensões, formatos ou estados.

Leia e registre os valores reais dos arquivos.

### **Passo 6 — Validar**

Antes de compactar, confirme:

- A quantidade total de imagens;

- A quantidade de registros do índice;

- A correspondência de uma linha por imagem;

- A exclusividade dos IDs;

- A continuidade da sequência;

- A conformidade dos nomes;

- A existência dos caminhos registrados;

- A legibilidade dos arquivos;

- A correspondência entre dimensões declaradas e reais;

- A preservação visual das fontes.

Interrompa o processo caso qualquer validação falhe.

Corrija a divergência e repita todas as validações afetadas.

### **Passo 7 — Compactar e testar**

Compacte a pasta raiz completa em um único arquivo ZIP.

O ZIP deve preservar a estrutura de pastas e conter:

- Todas as imagens;

- O MASTER_INDEX.csv;

- Este runbook.

Execute um teste de integridade do arquivo compactado.

Não entregue um ZIP que apresente avisos de corrupção, arquivos ausentes ou caminhos quebrados.

## **8. Critérios de aceite**

A entrega somente poderá ser considerada concluída quando:

- A quantidade de PNGs for igual à quantidade de linhas de dados do índice;

- Todo item_id for único;

- Todo item_id seguir o padrão SC-NNN;

- A sequência estiver completa e rastreável;

- Todo caminho registrado no CSV apontar para um arquivo existente;

- Nenhum nome possuir espaços;

- Nenhum nome possuir acentos;

- Nenhum nome possuir parênteses;

- Nenhum nome possuir duplicadores automáticos;

- As dimensões registradas corresponderem às dimensões reais;

- Todos os arquivos forem reconhecidos como imagens válidas;

- O teste de integridade do ZIP terminar sem erros;

- As imagens permanecerem visualmente idênticas às fontes quando o escopo for somente organizacional.

## **9. Solução de problemas**

| **Problema** | **Diagnóstico** | **Correção** |
| --- | --- | --- |
| Arquivo ausente | Uma linha do índice aponta para um caminho inexistente | Restaurar a fonte, reaplicar o nome e validar o caminho |
| ID duplicado | Dois itens compartilham a mesma identificação | Preservar a ordem e renumerar somente os itens conflitantes |
| Sequência quebrada | Existem lacunas ou repetições numéricas | Corrigir a numeração conforme a narrativa original |
| Dimensão divergente | O índice declara uma proporção diferente da imagem | Registrar os pixels reais ou solicitar redimensionamento separadamente |
| Imagem corrompida | O arquivo não é reconhecido como imagem válida | Recuperar a cópia original e substituir antes da compactação |
| ZIP inválido | O teste de integridade retorna erro | Gerar um novo ZIP a partir do diretório validado |
| Contexto ambíguo | A imagem pode pertencer a mais de uma pasta | Usar o objetivo editorial principal e registrar a decisão |
| Nome fora do padrão | O arquivo contém espaços, acentos ou duplicadores | Renomear conforme SC-NNN_TEMA_titulo-descritivo.png |
| Quantidades diferentes | O número de imagens não corresponde ao índice | Localizar itens ausentes ou registros excedentes antes da entrega |
| Proporção incorreta | A imagem foi declarada como 16:9 sem possuir essa dimensão | Registrar a dimensão real e escalar a conversão para uma tarefa autorizada |

## **10. Rollback**

Execute rollback quando:

- Uma imagem for perdida;

- Uma imagem for substituída incorretamente;

- O conteúdo visual for alterado sem autorização;

- A sequência narrativa for quebrada;

- O índice deixar de corresponder aos arquivos;

- O pacote final apresentar corrupção.

Procedimento de rollback:

- Interrompa a entrega.

- Não sobrescreva o pacote original.

- Preserve o pacote defeituoso para diagnóstico.

- Retorne à cópia original intacta.

- Reconstrua a estrutura canônica.

- Reaplique a classificação e a nomenclatura.

- Recrie o índice mestre.

- Repita todas as validações.

- Gere um novo ZIP.

- Registre a causa da falha.

## **11. Escalonamento**

Solicite decisão editorial antes de executar qualquer uma destas ações:

- Alterar títulos;

- Mudar a sequência narrativa;

- Mover uma peça entre contextos ambíguos;

- Converter imagens para 16:9;

- Recortar imagens;

- Redimensionar imagens;

- Corrigir textos incorporados às artes;

- Modificar cores;

- Alterar tipografia;

- Gerar novas imagens;

- Excluir peças;

- Substituir uma imagem aprovada.

A organização dos arquivos não autoriza alterações visuais.

## **12. Resultado padronizado desta execução**

| **Métrica** | **Resultado** |
| --- | --- |
| Imagens organizadas | 15 |
| Registros no índice | 15 |
| Pastas contextuais | 4 |
| Documentos operacionais | 2 |
| Alteração visual | Nenhuma |
| Validação final | Quantidade, caminhos e integridade do ZIP |
| Identificadores | SC-001 a SC-015 |
| Pacote final | PACOTE_SOBRECARGA_COGNITIVA_15_PADRONIZADO.zip |

## **13. Instrução final para o agente de IA**

Execute este runbook de forma sequencial.

Não pule etapas de inventário, indexação ou validação.

Não presuma que uma imagem possui proporção 16:9 apenas porque esse era o formato solicitado originalmente.

Utilize sempre as dimensões reais encontradas no arquivo.

Não altere o conteúdo visual sem autorização explícita.

Quando uma decisão editorial não puder ser determinada objetivamente, interrompa somente o item afetado, registre a pendência e solicite orientação.

Ao concluir, entregue:

- Um único diretório organizado por contexto;

- Todos os arquivos nomeados individualmente;

- Um MASTER_INDEX.csv com uma linha por imagem;

- Uma cópia deste runbook;

- Um único ZIP validado;

- Um relatório curto com quantidade de arquivos, quantidade de registros, pastas criadas, validações executadas e pendências.