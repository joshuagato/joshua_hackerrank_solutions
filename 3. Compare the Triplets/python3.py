#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    comparison_scores = [0, 0]
    
    for index in range(len(a)):
        if a[index] > b[index]:
            comparison_scores[0] += 1
        elif a[index] < b[index]:
            comparison_scores[1] += 1
        elif a[index] == b[index]:
            comparison_scores[0] += 0
            comparison_scores[1] += 0
    
    return comparison_scores

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
