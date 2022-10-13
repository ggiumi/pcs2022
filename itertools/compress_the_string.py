from itertools import groupby
for k, S in groupby(input()):
  print((len([i for i in S]), int(k)), end=' ')
