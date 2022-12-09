with open("rosalind_perm.txt") as f:
    seq = int(f.readline().strip())
from itertools import permutations
n = []
for i in range(seq):
    n.append(i+1)
possible_perm = list(permutations(n))
print(len(possible_perm))
for j in possible_perm:
    print(f"{' '.join(str(i)for i in j)}")