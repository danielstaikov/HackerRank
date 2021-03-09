n = int(input())
integer_list = map(int, input().split())
currentTuples = tuple(integer_list)
print(hash(currentTuples))