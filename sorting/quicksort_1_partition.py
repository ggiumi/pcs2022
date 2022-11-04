import math
import os
import random
import re
import sys

def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = []
    for i in arr:
        if i < arr[0]:
            left.append(i)
        elif i > arr[0]:
            right.append(i)
        else:
            equal.append(i)
    return(left + equal + right)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()