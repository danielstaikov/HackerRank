#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'commonSubstring' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#

def commonSubstring(a, b):
    # Write your code here

    for i in range(len(a)):
        answer = None
        lookFor = a[i]
        lookIn = b[i]
        for i in lookFor:
            result = lookIn.find(i)
            if result != -1:
                answer = True
        if answer:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    commonSubstring(a, b)
