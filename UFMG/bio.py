from Bio import Entrez
''' Isso primeiramente é a coleta dos dados, precisa do email pra acessar e com a função do esearch,
ele retorna a lista de ids que correspondem com a consulta'''

Entrez.email="gabifalcao2102@gmail.com" 

search=Entrez.esearch(
    db="protein",
    term="Tenebrio molitor[Organism]",
    retmax=20
)
record= Entrez.read(search)
ids=record["IdList"]

search= Entrez.efetch( # com o efetch, recupera os registros e baixa eles 

    db="protein",
    id=ids,
    rettype="gb",
    retmode="text"
)
from Bio import SeqIO # esse é o parsing, vai extrair o contéudo

records= list(SeqIO.parse(search, "genbank"))

for record in records:
    print(record.id)
    print(len(record.seq))
    print(record.annotations.get("organism"))

unique_sequences = {} #dicionario hash table(estrutura de dados)

for record in records:
    seq = str(record.seq)
    if seq not in unique_sequences:
        unique_sequences[seq] = record


SeqIO.write(unique_sequences.values(), "proteins.fasta", "fasta") # vai retornar um arquivo fasta, ou seja, os dados. 