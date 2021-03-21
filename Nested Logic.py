returnedDate = map(int, input().split())
dueDate = map(int, input().split())
fine = 0
returnedList = list(returnedDate)
dueList = list(dueDate)
if dueList[2] < returnedList[2]:
    fine = 10000
elif dueList[2] == returnedList[2]:
    if dueList[1] < returnedList[1]:
        fine = 500*(returnedList[1]-dueList[1])
    else:
        if dueList[0] < returnedList[0]:
            fine = 15*(returnedList[0]-dueList[0])

print(fine)

# x = datetime.datetime(2018, 9, 15)
# Sep 15 2018 00:00:00