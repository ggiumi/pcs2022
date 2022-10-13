def average(array):
    # your code goes here
    n = set(array)
    return sum(n)/len(n) 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)