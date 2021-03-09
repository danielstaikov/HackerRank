def count_substring(string, sub_string):
    lenghtSub = len(sub_string)
    lenghtString = len(string)
    count = 0
    for i in range(lenghtString - lenghtSub+1):
        comp = string[i:i+lenghtSub]
        if comp == sub_string:
            count += 1
    return count

# ABCDCDC
# CDC


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)