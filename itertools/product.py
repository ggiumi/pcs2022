from itertools import product
a = input().split()
b = input().split()
AxB = list(product(a, b))

for i in AxB:
    print('({}, {})'.format(i[0], i[1]),end=' ')