with open("rosalind_lia.txt") as f:
    seq = f.readlines()
    splitted = seq[0].split(' ')
import math
N = int(splitted[0])
k = int(splitted[1])
gen = 2**N
counter_prob = 0
for i in range(k, gen+1):
    prob = (math.factorial(gen)/(math.factorial(i)*math.factorial(gen-i)))*(0.25**i)*(0.75**(gen-i))
    counter_prob += prob
print(counter_prob)
