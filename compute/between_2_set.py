#!/bin/python3
import math
import os
import sys

#
# Complete the getTotalX function below.
#
def isFactorOfSet(a, set_b):
    for b in set_b:
        if b % a !=0:
            return False
    
    return True

def isSetFactorOfNum(set_a, b):
    for a in set_a:
        if b % a !=0:
            return False
    
    return True

def getTotalX(a, b):
    # assumption: find the factors between max_a and min_b
    max_a = max(a)
    min_b = min(b)

    div = int(min_b / max_a)
    candidates = [max_a * di for di in range(1, div + 1)]
    print(candidates)
    num = 0

    for candidate in candidates:
        print(candidate, a, b)
        if isFactorOfSet(candidate, b):
            
            if isSetFactorOfNum(a, candidate):
                
                num += 1
                    
    
    return num


    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()



