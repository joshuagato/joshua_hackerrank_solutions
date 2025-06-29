#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        # Number of spaces before '#'
        num_spaces = n - i
        # Number of '#' symbols
        num_hashes = i
        
        # Print spaces followed by hashes
        print(" " * num_spaces + "#" * num_hashes)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
