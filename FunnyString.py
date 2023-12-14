#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
  rev = s[::-1]
  listA = []
  listB = []
  absA = []
  absB = []

  for i in s:  
      listA.append(ord(i))
  for j in rev:
      listB.append(ord(j))
    
  for k in range(len(listA)-1):
    absA.append(abs(listA[k]-listA[k+1]))
    absB.append(abs(listB[k]-listB[k+1]))
    
      
    
  if (absA == absB):
      return "Funny"
  else:
      return "Not Funny"
    

    # Write your code here

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)
        print(result)


   
