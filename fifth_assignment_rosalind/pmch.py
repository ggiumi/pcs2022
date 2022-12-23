from Bio import SeqIO
from math import factorial
fasta = []
sequence = []
with open ("rosalind_pmch.txt") as fa:
    for seq_record in SeqIO.parse(fa,'fasta'):
        fasta.append(str(seq_record.name))
        sequence.append(str(seq_record.seq))
seq = (' '.join(sequence))
perfect_matching = factorial(seq.count("A")) * factorial((seq.count("C")))
print(perfect_matching)