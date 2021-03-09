# 5
# 2 3 6 6 5
n = int(input())
arr = list(input().split())
nums = []
for i in arr:
    nums.append(int(i))
maxArr = max(nums)
runnerUp = []
for i in nums:
    if i<maxArr:
        runnerUp.append(i)
print(max(runnerUp))