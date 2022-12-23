from Bio import SeqIO
fasta = []
seq = []
with open ("rosalind_sseq.txt") as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        fasta.append(str(seq_record.name))
        seq.append(str(seq_record.seq))
s = seq[0]
t = seq[1]
def sseq(s, t):
    x = 0
    for i in t:
        y = s.find(i, x)
        x = y+1
        print(x, end=' ')
sseq(s, t)