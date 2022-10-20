from collections import defaultdict

n,m = input().split()
A = {}    
B = {}

for i in range(int(n)):
    integer = input()
    if integer in A:
        A[integer].append(str(i+1))
    else:
        A[integer] = [str(i+1)]

for i in range(int(m)):
    integer = input()
    if integer in A:
        print(' '.join(A[integer]))
    else:
        print('-1')