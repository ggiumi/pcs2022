from Bio.Seq import Seq
with open('rosalind_splc.txt') as f:
    introns = []
    f = f.read().split('>')[1:]
    seq = str(f[0]).split('\n', 1)[1].replace('\n', '')
    for i in range(1, len(f)):
        intron = f[i].split('\n', 1)[1].replace('\n', '')
        introns.append(intron)
def splc(seq, introns):
    for intron in introns:
        seq = seq.replace(intron, '')
    dna = Seq(seq)
    protein = dna.translate(to_stop = True)
    return(protein)
print(splc(seq, introns))