from Bio import SeqIO
fasta = []
seq = []
with open ("rosalind_long.txt") as fa:
    for seq_record in SeqIO.parse(fa,'fasta'):
        fasta.append(str(seq_record.name))
        seq.append(str(seq_record.seq))
superstring = seq[0]
def overlap(seq, superstring):
    for i in seq:
        for j in range(len(i)//2):
            overlap = len(i) - j
            if superstring.startswith(i[j:]):
                return i, i[:j] + superstring
            if superstring.endswith(i[:overlap]):
                return i, superstring + i[overlap:]
def shortest(seq, superstring):
    while True:
        i, superstring = overlap(seq, superstring)
        seq.remove(i)
        if len(seq) == 0:
            return superstring
shortest_superstring = shortest(seq, superstring)
print(shortest_superstring)