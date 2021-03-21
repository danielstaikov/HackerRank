#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swapCount = 0
while True:
    swapped = False
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            swapped = True
            swapCount +=1
    if not swapped:
        break

print(f'Array is sorted in {swapCount} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')