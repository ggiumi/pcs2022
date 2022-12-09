with open('rosalind_lgis.txt') as f:
    num = int(f.readline().strip())
    list1 = list(f.readline().strip().split())
seq = [eval(i) for i in list1]
a = [0]*num
for k in range(num-2, -1, -1):
    for j in range(num-1, k, -1):
        if seq[k] < seq[j] and a[k] <= a[j]:
            a[k] += 1
    max1 = max(a)
    inc = []
    for i in range(num):
        if a[i] == max:
            inc.append(seq[i])
            max1 -= 1
b = [0]*num
for x in range(num-2, -1, -1):
    for y in range(num-1, x, -1):
        if seq[x] > seq[y] and b[x] <= b[y]:
            b[x] += 1
    max2 = max(b)
    dec = []
    for i in range(num):
        if b[i] == max2:
            dec.append(seq[i])
            max2 -= 1
print(' '.join(map(str, inc)))
print(' '.join(map(str, dec)))