from collections import namedtuple

n = int(input())
student = namedtuple('Student', ",".join(input().split()))
print(sum([int(student(*input().split()).MARKS) for _ in range(n)])/n)
