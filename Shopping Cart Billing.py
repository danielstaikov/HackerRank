#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findLowestPrice' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_STRING_ARRAY products
#  2. 2D_STRING_ARRAY discounts
#

def findLowestPrice(products, discounts):
    # Write your code here
    p = products
    d = discounts
    bill = 0
    for i in p:
        currentProduct = i
        minPrice = 99999
        currentPrice = 0
        for j in range(1, len(currentProduct)):
            for k in d:
                if currentProduct[j] == k[0]:
                    discountType = int(k[1])
                    amount = int(k[2])
                    if discountType == 0:
                        currentPrice = amount
                    elif discountType == 1:
                        currentPrice = round(currentPrice - currentPrice*amount/100)
                    elif discountType == 2:
                        currentPrice = round(currentPrice - amount)
                if currentPrice <= minPrice:
                    minPrice = currentPrice
        bill = bill + minPrice
    print(bill)

if __name__ == '__main__':
# Input:
# 2
# 3
# 10 sale january-sale
# 200 sale
# 2
# 3
# sale 0 10
# january-sale 1 10

    products_rows = int(input().strip())
    products_columns = int(input().strip())

    products = []

    for _ in range(products_rows):
        products.append(input().rstrip().split())

    discounts_rows = int(input().strip())
    discounts_columns = int(input().strip())

    discounts = []

    for _ in range(discounts_rows):
        discounts.append(input().rstrip().split())

    result = findLowestPrice(products, discounts)

    str(result)
