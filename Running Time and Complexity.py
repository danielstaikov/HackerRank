import math

numbers = int(input())
for i in range(numbers):
    token = int(input())
    limit = int(math.sqrt(token))
    isPrime = True
    if token == 1:
        print("Not prime")
    else:
        for n in range(2, limit+1):
            if token % n == 0:
                isPrime = False
                break
            else:
                isPrime = True
        if isPrime:
            print("Prime")
        else:
            print("Not prime")

# input
# 3
# 1000000007
# 100000003
# 1000003
# 9223372036854775807
