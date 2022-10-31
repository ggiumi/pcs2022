import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))
    return
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)