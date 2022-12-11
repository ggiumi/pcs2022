with open("rosalind_lcsm.txt") as f:
    seq = f.read().splitlines()
for position in range(len(seq)):
    if seq[position].startswith(('>')):
        fasta = (seq[position])
    else:
        sequence = (seq[position])
list = []
common_sub = ''
find = ''
for i in range(len(sequence[0])):
    find += list[0][i]
    check = True
    for j in sequence:
        if find not in j:
            find = ''
            check = False
            common_sub = find
lcsm = max(list, key = len)
print(lcsm)