# Entrez_Bio
## Esse reposítorio foi feito para colocar scripts iniciais da ultilização do Entrez Programing Utilities e o uso da biblioteca de Biopython 
---
O arquivo principal é o "bio.py". O conteúdo foi feito para a curadoria de sequências de proteínas repetidas em registros diferentes, sem ultilizar o recurso IPG (identical protein groups) disponibilizado pelo NCBI.  
_Explicação do que foi feito:_
No ínicio, da blibioteca Biopython baixada previamente, se importa o módulo Entrez, que permite o acesso ao NCBI de maneira programável por meio do _WWW_, assim conecta com a API do NCBI, logo após o e-mail, que tem que ter para não dar problema no acesso, a funcão _Esearch_ e a variável é declarada. Ela procura, como diz o nome, e retorna um conjunto de identificadores (IDs) que correspondem ao termo pesquisado para um uso futuro. Os parâmetros, db (banco de dados que queira retirar as informações), term ( texto a ser pesquisado, podendo ser organismos, palavras-chave, etc) e retmax (número máximo de registros que o NCBI deve retornar e por padrão o entrez retorna 20). 
Após isso o _Read_ parseia o arquivo de informações retiradas com o Esearch que está em XML e transforma em um objeto em python para retornar um dado estruturado de lista, sendo um elemento Dicionário permitindo acesso estruturado aos IDs recuperados. A variável é uma estrutura indexada e acessa a lista e isso propõe acesso dinâmico a propriedade de um objeto string, assim permitindo o acesso e a ultilização em etapas posteriores.
Com o _Efetch_, se recupera os registros completos correspondentes aos IDs obtidos, retorna um objeto do tipo _handle_, que representa o fluxo de dados recebido do NCBI. Os parâmetros são declarados novamente porque cada função é idependente e envia uma requisitação HTTP distinta e completa para o servidor do NCBI, então precisa ser explicito em qual bando de dados buscar os IDs fornecidos.
O _rettype_ define o formato do aquivo ou o tipo de dado, tem FASTA, XML no caso é o GB que é o registro completo no formato Genbank e ele trabaha junto com o _retmode_ que especifíca o formato da sa´da que no caso é TEXT podendo ser XML também. 
Do Biopython importa o pacote _SeqIO_, a função Seq.IO.parse() é a principal função do pacote, permite a leitura dos registros e a partir do laço armazena a variável records e le as informações do arquivo que são: id, sequência e a anotação com o auxílio da função _len_. O objeto _handle_ retornado pelo _efetch_ é passado para _SeqIO.parse_, que ionterpreta os registros no "genbank" e retorna um iterator, que permite percorrer os registros de um a um, sem carregar todo o conteúdo de uma vez na memória, o  _SeqRecord_.
A _unique_sequences_ é um dicionário (que para poder comparar diretamente tem que transformar a sequência  em uma string) utilizado para armazenar sequências únicas. Com essa comparação o programa vê se a sequência já apareceu ou não. Se é única, adiciona na record. 
O output do objeto SeqRecord, _SeqIO.write_ grava os registros armazenados no dicionário em um arquico FASTA  e o método  _values_  retorna apenas os objetos SeqRecord armazenados como valores no dicionário.

---
## Considerações: 
### Essas etapas iniciais estabelecem a base para a construção de uma pipeline automatizada de curadoria de dados biológicos. 
+ Os parâmetros ultilizaddos ainda são limitados em relação ao volume real de dados disponíveis no Genbank. Com os testes inciais já indicam a possibilidade de trabalhar com milhares de sequências, o que sugere que no futuro usar armazenamento local para não depender de requisitar o NCBI.
+ O método atual de remoção de duplicatas considera apenas sequências idênticas, altamente similares ou variantes podem não ser removidas.
+ Implementar extração de features a partir dos registros com o objetivo de estruturar os dados para análisees conmputacionais e e futura aplicação de modelos de machine learning. 

