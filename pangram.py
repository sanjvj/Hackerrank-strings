#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    setA = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '}
    setB = set()

    

    s=s.lower()

    for i in s:
        setB.add(i)
    
    if(setA == setB):
       return "pangram"
    else:
      return "not pangram"

if __name__ == '__main__':
    

    s = input()

    result = pangrams(s)

    print(result);

  
