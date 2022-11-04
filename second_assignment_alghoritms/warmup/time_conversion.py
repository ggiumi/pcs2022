import math
import os
import random
import re
import sys

def timeConversion(s):
    new = ""
    s = s.split(":")
    if "PM" in s[2]:
        if s[0] =="12":
            new = "12"
        else:
            new = str(int(s[0])+12)
        new += ":"+s[1]+":"+s[2][:2]
    else:
        if s[0] == "12":
            new = "00"
        else:
            new = s[0]
        new += ":"+s[1]+":"+s[2][:2]
        
    return (new)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()