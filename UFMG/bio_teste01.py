from Bio import Entrez

Entrez.email="gabifalcao2102@gmail.com" 

search=Entrez.esearch(
    db="protein",
    term="Tenebrio molitor[Organism]",
    retmax=20
)
record= Entrez.read(search)
ids=record["IdList"]

search= Entrez.efetch(
    db="protein",
    id=ids,
    rettype="gb",
    retmode="text"
)
from Bio import SeqIO

records= list(SeqIO.parse(search, "genbank"))

for record in records:
    print(record.id)
    print(len(record.seq))
    print(record.annotations.get("organism"))

unique_sequences = {} 

for record in records:
    seq = str(record.seq)
    if seq not in unique_sequences:
        unique_sequences[seq] = record

total = len(records)
unique = len(unique_sequences)

print(f"Total: {total}")
print(f"Unique: {unique}")

with open("log.txt", "a") as f:
    f.write(f"Total sequences: {total}\n")
    f.write(f"Unique sequences: {unique}\n") 

SeqIO.write(unique_sequences.values(), "proteins.fasta", "fasta")