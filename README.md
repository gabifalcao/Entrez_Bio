# Entrez_Bio
## Esse reposítorio foi feito para colocar scripts iniciais da ultilização do Entrez Programing Utilities e o uso da biblioteca de Biopython 
---
O arquivo principal é o "bio.py". O conteúdo foi feito para a curadora de sequências de proteínas repitidas em registros diferentes, sem ultilizar o recurso IPG (identical protein groups) disponibilizado pelo NCBI.  
-Explicação do que foi feito:-
No ínicio, da blibioteca Biopython baixada previamente, se importa o módulo Entrez, que permite o acesso ao NCBI de maneira programável por meio do -WWW-, assim conecta com a API do NCBI, logo após o e-mail, que tem que ter para não dar problema no acesso, a funcão -Esearch- e a variável é declarada. Ela procura, como diz o nome, e enclasura as IDS para um uso futuro. Os parâmetros, db (banco de dados que queira retirar as informações), term ( texto a ser pesquisado, podendo ser organismos, palavras-chave, etc) e retmax (número máximo de registros que o NCBI deve retornar e por padrão o entrez retorna 20). 
