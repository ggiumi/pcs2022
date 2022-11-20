from Bio import SeqIO
from collections import Counter
import pandas as pd

lst = []
for x in SeqIO.parse('rosalind_cons.txt', 'fasta'):
    lst.append(x.seq)

lst_cnt = []
for pos in range(len(lst[0])):
    new_lst = []
    for seq in lst:
        new_lst.append(seq[pos])
        
    lst_cnt.append(Counter(new_lst))

for pos in range(len(lst_cnt)):
    print(lst_cnt[pos].most_common()[0][0], end='')

print()

dft = pd.DataFrame(lst_cnt, columns=['A', 'C', 'G', 'T']).fillna(0).T
for symbol in ['A', 'C', 'G', 'T']:
    print(symbol, end=': ')
    dft.loc[symbol].apply(lambda row: print(int(row), end=' '))
    print()