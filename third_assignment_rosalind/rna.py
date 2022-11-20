with open("rosalind_rna.txt") as f:
    seq = (f.readlines())
rna_seq = seq[0].replace("T", "U")
print(rna_seq)