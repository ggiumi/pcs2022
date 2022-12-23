from Bio import SeqIO
fasta = []
seq = []
transition = 0
transversions = 0
with open ("rosalind_tran.txt") as fa:
    for seq_record in SeqIO.parse(fa,'fasta'):
        fasta.append(str(seq_record.name))
        seq.append(str(seq_record.seq))
transition_list = [('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')]
transversions_list = [('A', 'T'), ('A', 'C'), ('T', 'A'), ('T', 'G'), ('C', 'A'), ('C', 'G'), ('G', 'T'), ('G', 'C')]
s1, s2 = seq
for i in range(len(s1)):
    if (s1[i], s2[i]) in transition_list:
        transition += 1
    if (s1[i], s2[i]) in transversions_list:
        transversions += 1
ratio = (transition/transversions)
print(ratio)