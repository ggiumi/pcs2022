import math
import os
import random
import re
import sys

def camelcase(s):
    counter = 1
    for i in s:
        if (i.isupper()):
            counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()