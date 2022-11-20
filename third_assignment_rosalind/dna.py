from collections import Counter
with open("rosalind_dna.txt") as f:
    seq = str(f.readlines())
print((str(seq.count("A")) + " " + str(seq.count("C")) + " " + str(seq.count("G")) + " " + str(seq.count("T"))))