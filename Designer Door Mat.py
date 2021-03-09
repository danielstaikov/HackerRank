# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# string.center(length, character)

inputToken = input().split()
n = int(inputToken[0])
m = int(inputToken[1])
horisontalMid = (n//2)
fillchar = '-'
vertMidPattern = ".|."
for i in range(horisontalMid):
    s = (i*2+1)*vertMidPattern
    print(s.center(m, fillchar))
print("WELCOME".center(m, fillchar))
for i in range((horisontalMid - 1), -1, -1):
    s = (i*2+1)*vertMidPattern
    print(s.center(m, fillchar))
