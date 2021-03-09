students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student = [name, score]
    students.append(student)
sorted_grades = sorted(students, key=lambda kvp: (kvp[1], kvp[0]))
minGrade = sorted_grades[0]
secondGradeNames = []
for i in sorted_grades:
    if i[1] != minGrade[1]:
        secondGradeNames.append(i)
minSecondGrade = secondGradeNames[0]
for i in secondGradeNames:
    if i[1] == minSecondGrade[1]:
        print(i[0])