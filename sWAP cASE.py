def swap_case(list):
    listOfCars = []
    listOfCars[:0] = list
    swapCaseList = []
# isupper(), islower(), isalpha()
    for i in listOfCars:
        currentLetter = i
        if currentLetter.isalpha():
            if currentLetter.isupper():
                currentLetter = currentLetter.lower()
            elif currentLetter.islower():
                currentLetter = currentLetter.upper()
        swapCaseList.append(currentLetter)
        swapCase = "".join(swapCaseList)
    return swapCase


# hACKERrANK.COM PRESENTS "pYTHONIST 2".
s = input()
result = swap_case(s)
print(result)