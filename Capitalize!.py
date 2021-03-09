#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    capFullName = []
    regex = r"(?:\w+\s*)"
    matches = re.finditer(regex, s, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):

        capFullName.append(str(match.group()).capitalize())
    result_01 = " ".join(capFullName)
    print(result_01)
#    return result_01

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

#    fptr.write(result + '\n')

 #   fptr.close()
