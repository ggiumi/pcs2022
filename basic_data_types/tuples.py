if __name__ == 'main':
    N = input()
    tup = tuple((int(x) for x in input().split()))
    print(hash(tup))