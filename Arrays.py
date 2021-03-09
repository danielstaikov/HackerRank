#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input())

arr = list(map(int, input().rstrip().split()))
arr.reverse()
print(" ".join(str(s) for s in arr))
