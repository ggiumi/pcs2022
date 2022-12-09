with open("rosalind_mrna.txt") as f:
    seq = f.readline().strip()
possible_proteins = {'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4}
possible_translation = 1
for i in seq:
    possible_translation *= (possible_proteins[i])
print(possible_translation*3%1000000)