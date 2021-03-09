# for letter in letters:
# number = ord(letter) - 96
# numbers.append(number)
# ascii = chr(number)
# string.center(length, character)

# print(numbers)

def print_rangoli(size):
    letters = []
    for i in range(size, 0, -1):
        letter = chr(i + 96)
        letters.append(letter)
    print(letters)
    s = []
    for letter in letters:
        s.append(letter + "-")
    for i in range(len(s)):
        row = []
        num = (size-i-1)*2
        row.append("-"*num)
        for j in range(i+1):
            row.append(s[j])
        for k in range(i):
            row.append(s[size-1-k])
        row.append("-"*num)
        result = "".join(row)
        print(result[:-1])
    for i in range(len(s)-1, 0, -1):
        num = (size-i)*2
        print("-"*num, end="")
        for j in range(i):
            print(s[j], end="")
        print()

# your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)