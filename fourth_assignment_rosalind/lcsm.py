with open("rosalind_lcsm.txt") as f:
    seq = f.read().splitlines()
for position in range(len(seq)):
    if seq[position].startswith(('>')):
        fasta = (seq[position])
    else:
        sequence = (seq[position])
first_seq = min(sequence, key=len)
k = len(first_seq)
for i in range(k, 1, -1):
    for j in range(k-i+1):
        motif = first_seq[j:j+i]
        found = True           
        for seq in sequence:
            s = seq.find(motif)
            if s == -1:
                found = False
                break
            if found == True:
                print(motif)