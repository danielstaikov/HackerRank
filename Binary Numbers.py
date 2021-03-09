#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binaryRep = ("{0:b}".format(n))
    print(binaryRep)
    total = 0
    count = 1
    for i in range(1, len(binaryRep)):
        if binaryRep[i] == "1":
            count += 1
        else:
            count = 0
        if total <= count:
            total = count
    print(total)
