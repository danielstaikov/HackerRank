def split_and_join(line1):
    # write your code here
    result = line1.strip()
    result = result.split(" ")
    result = "-".join(result)
    return result


line = input()
result = split_and_join(line)
print(result)