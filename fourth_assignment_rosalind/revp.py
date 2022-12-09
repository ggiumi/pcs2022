with open("rosalind_revp.txt") as f:
    seq = f.read().split("\n")
dna_seq = ''.join(seq[1:-1])
length = [4, 6, 8, 10, 12]
for i in range(len(dna_seq)):
    for j in length:
        if i + j <= len(dna_seq):
            sub = dna_seq[i:i+j]
            reverse = sub[::-1].replace("A", "%temp%").replace("T", "A").replace("%temp%", "T").replace("C", "%temp%").replace("G", "C").replace("%temp%", "G")
            if sub == reverse:
                print(str(i+1) + " " +str(len(reverse)))