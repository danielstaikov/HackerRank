# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

inputToken = int(input())
for i in range(inputToken):
    output = i+1
    pad = ("{0:b}".format(inputToken))
    print(str(output).rjust(len(pad), " ") + " " + "{0:o}".format(output).rjust(len(pad), " ") + " " + "{0:X}".format(output).rjust(len(pad), " ") + " " + "{0:b}".format(output).rjust(len(pad), " "))
