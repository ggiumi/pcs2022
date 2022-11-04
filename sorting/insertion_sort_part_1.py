import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    for i in range((n-1),0,-1):
        if arr[i] < arr[i-1]:
            tmp = arr[i]
            arr[i] = arr[i-1]
            print(*arr)
            arr[i-1] = tmp
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)