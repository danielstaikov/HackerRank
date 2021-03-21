import sys

class Solution:
# Write your code here

    def pushCharacter(self, data):
        stack.append(data)
    def enqueueCharacter(self, data):
        queue.append(data)
    def popCharacter(self):
        return stack.pop()
    def dequeueCharacter(self):
        return queue.pop(0)


stack = []
queue = []
# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    stackPop = obj.popCharacter()
    queuePop = obj.dequeueCharacter()
    if stackPop != queuePop:
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
