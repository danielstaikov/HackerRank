
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    n=2
    maxSum = -sys.maxsize - 1
    for c in range(4):
        for i in range(4):
            amount = 0
            for j in range(c, c+n+1):
                amount = amount + arr[i][j]
            amount = amount + arr[i+1][c+1]
            for j in range(c, c+n+1):
                amount = amount + arr[i+2][j]
            if amount >= maxSum:
                maxSum = amount
    print(maxSum)
