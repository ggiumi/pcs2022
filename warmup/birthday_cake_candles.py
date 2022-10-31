import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    counter = 0 
    bigger_candles = max(candles)
    for i in range(len(candles)):
        if bigger_candles == candles[i]:
            counter +=1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()