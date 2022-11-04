import math
import os
import random
import re
import sys

def superReducedString(s):
    for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                return superReducedString(s[:i]+s[i+2:])
    else:
            if len(s) == 0:
                return "Empty String"
            return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()