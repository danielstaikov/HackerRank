import textwrap

def wrap(string, max_width):
    wraped = textwrap.wrap(string, max_width)
    print(*wraped, sep="\n")
    return "\n"


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)