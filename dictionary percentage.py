n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
records = student_marks[query_name]
lengthRecords = len(records)
percentage = sum(records)/lengthRecords
print('{:.2f}'.format(percentage))
