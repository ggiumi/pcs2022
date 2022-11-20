with open("rosalind_prob.txt") as f:
    seq = f.read().splitlines()
    import math
for i in seq:
    if i[0] != 'A' and i[0] != 'T' and i[0] != 'G' and i[0] != 'C':
            array = i.split()
            gc_content = []
            for j in array:
                gc_content.append(float(j))
match_probs = []
for i in range(len(gc_content)):
    prob = math.log10((((1 - gc_content[i])/2)**(seq[0].count('A')+seq[0].count('T')))*(gc_content[i]/2)**(seq[0].count('G')+seq[0].count('C')))
    match_probs.append('%0.3f' % prob)
print(*match_probs, end = ' ')