from Bio import SeqIO
fasta = []
sequence = []
with open ('rosalind_grph.txt','r') as fa:
    for seq_record in SeqIO.parse(fa,'fasta'):
        fasta.append(str(seq_record.name))
        sequence.append(str(seq_record.seq))
'''print(sequence) 
print(fasta)'''
for i in range(len(sequence)):
    for j in range(len(sequence)):
        if i != j and sequence[i][-3:] == sequence[j][:3]:
            print(fasta[i], fasta[j])