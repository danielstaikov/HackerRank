# alphanumeric characters - str.isalnum()
# alphabetical characters - str.isalpha()
# digits - str.isdigit()
# lowercase - str.islower()
# uppercase characters - str.isupper()

s = input()
alfa = False
digi = False
lowe = False
upper = False
for i in s:
    if i.isalpha():
        alfa = True
    elif i.isdigit():
        digi = True
    if i.islower():
        lowe = True
    elif i.isupper():
        upper = True
if alfa or digi:
    print(True)
else:
    print(False)
print(alfa)
print(digi)
print(lowe)
print(upper)

