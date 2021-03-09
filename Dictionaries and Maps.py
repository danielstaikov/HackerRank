rows = int(input())
phoneBook = {}
for i in range(rows):
    inputToken = input().split()
    current = dict([(inputToken[0], inputToken[1])])
    phoneBook.update(current)
while True:
    try:
        asq = input()
        if asq in phoneBook:
            print(asq+"="+phoneBook[asq])
        else:
            print("Not found")
    except:
        break
