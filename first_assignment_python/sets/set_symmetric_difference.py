e = int(input())
eng = set(list(map(int, input().split())))
f = int(input())
fran= set(list(map(int, input().split())))
neither = eng.symmetric_difference(fran)
print(len(neither))