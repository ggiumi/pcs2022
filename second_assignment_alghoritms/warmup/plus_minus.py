import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos = list()
    neg = list()
    zero = list()
    
    for _ in arr:
        if _ > 0:
            pos.append(_)
        elif _ < 0:
            neg.append(_)
        else:
            zero.append(_)
    
    print("%06f" % (len(pos)/len(arr)))
    print("%06f" % (len(neg)/len(arr)))
    print("%06f" % (len(zero)/len(arr)))
    
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)