def mutate_string(string, position, character):
    listOfString = [char for char in string]
    # insert(i, x)
    # pop([i])
    # abracadabra
    listOfString.pop(position)
    listOfString.insert(position, character)
    newString = "".join(listOfString)
    return newString


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)