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

data = []

for record in unique_sequences.values():
    data.append({
        "id": record.id,
        "length": len(record.seq),
        "organism": record.annotations.get("organism"),
        "num_features": len(record.features)
    })

with open ("dados", "w") as f:

    f.write(f"Dados: {data}")
    


SeqIO.write(unique_sequences.values(), "proteins.fasta", "fasta")
