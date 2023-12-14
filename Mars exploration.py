#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    original = 'SOS'
    number = len(s)//3
    total = 'SOS'*number
    count = 0
    for i in range(len(s)):
      if s[i]!=total[i]:
        count+=1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
