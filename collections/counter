from collections import Counter

x = input()
sz = input().split()
N = int(input())
buyer = []

for _ in range(N):
    buyer.append(input().split())
pair = Counter(sz)
money = 0

for i in buyer:
    if i[0] in pair.keys() and pair[i[0]] != 0:
        money += int(i[1])
        pair[i[0]] -= 1
print(money)         
