import math
import os
import random
import re
import sys

def closestNumbers(arr):
    sortedarr = sorted(arr)
    result = []
    minimum = sortedarr[1] - sortedarr[0]
    for i in range (1, len(sortedarr)):
        difference = sortedarr[i] - sortedarr[i-1]
        if difference == minimum: 
            result.extend([sortedarr[i-1], sortedarr[i]])
        elif difference < minimum: 
            minimum = difference 
            result = [sortedarr[i-1], sortedarr[i]]
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
