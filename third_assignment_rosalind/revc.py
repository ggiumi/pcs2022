with open("rosalind_revc.txt") as f:
    seq = (f.readlines())
rna_seq = seq[0].replace("A", "%temp%").replace("T", "A").replace("%temp%", "T").replace("C", "%temp%").replace("G", "C").replace("%temp%", "G")
print(rna_seq[::-1])