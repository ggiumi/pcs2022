import math
import os
import random
import re
import sys

def findMedian(arr):
    sorted_arr = sorted (arr)
    median = sorted_arr[int((n-1)/2)]
    return median
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()