num = int(input())
for i in range(num):
    odd = ""
    even = ""
    inputToken = input()
    for i in range(len(inputToken)):
        if i%2 == 0:
            even += inputToken[i]
        else:
            odd += inputToken[i]
    print(even + " " + odd)
