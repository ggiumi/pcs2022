
with open("rosalind_pper.txt") as f:
    seq = f.readlines()
    splitted = seq[0].split(' ')
n = int(splitted[0])
k = int(splitted[1])
m = (n-k)
fact = 1
for i in range(1, n+1):
    fact = fact*i
fact2 = 1
for j in range(1, m+1):
    fact2 = fact2*j
partial_perm = fact/fact2 % 1000000
print(int(partial_perm))