with open("rosalind_lexf.txt") as f:
    seq = f.read().splitlines()
from itertools import product
symbols = seq[0]
n = int(seq[1])
ordered_symbols = symbols.replace(' ', '')
list = (product(ordered_symbols, repeat=n))
for i in list:
    print(''.join(i))