with open("rosalind_revp.txt") as f:
    seq = f.read().splitlines()
for position in range(len(seq)):
    if seq[position].startswith(('>')):
        fasta = (seq[position])
    else:
        sequence = (seq[position])
def reverse_translation(seq):
    translation = str.maketrans('ATCG','TAGC')
    complement_strand = seq.translate(translation)[::-1]
    return complement_strand
result=[]
for i in range(len(sequence)):
    for j in range(4,13):
        if i + j > len(sequence):
            continue
        string1 = sequence[i:i+j]
        string2 = reverse_translation(string1)
        if string1 == string2:
            result.append((i+1, j))
print("\n".join([' '.join(map(str, r)) for r in result]))