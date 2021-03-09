# insert i e: Insert integer e at position i
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
N = int(input())
item = []
for i in range(N):
    inputToken = input().split()
    if inputToken[0] == "insert":
        index = int(inputToken[1])
        if index <= len(item)-1:
            item.insert(index, int(inputToken[2]))
        else:
            item.append(int(inputToken[2]))
    elif inputToken[0] == "print":
        print(item)
    elif inputToken[0] == "remove":
        item.remove(int(inputToken[1]))
    elif inputToken[0] == "append":
        item.append(int(inputToken[1]))
    elif inputToken[0] == "sort":
        item.sort()
    elif inputToken[0] == "pop":
        item.pop(-1)
    elif inputToken[0] == "reverse":
        item.reverse()
    else:
        print("Input is not correct!")
