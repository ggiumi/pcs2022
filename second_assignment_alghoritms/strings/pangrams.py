import math
import os
import random
import re
import sys

def pangrams(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    s= s.lower()
    s = s.replace(" ","")
    s = sorted(s)
    for i in s:   
        if i == alphabet[counter]:
            counter += 1
        if counter == len(alphabet):
            return("pangram")
    else:
        return("not pangram")

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close