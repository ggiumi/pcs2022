from Bio import SeqIO
fasta = []
seq = []
with open ('rosalind_grph.txt','r') as fa:
    for seq_record in SeqIO.parse(fa,'fasta'):
        fasta.append(str(seq_record.name))
        seq.append(str(seq_record.seq))
for i in range(len(seq)):
    for j in range(len(seq)):
        if i != j and seq[i][-3:] == seq[j][:3]:
            print(fasta[i], fasta[j])