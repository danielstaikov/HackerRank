text, lookup_text = input(), input()

occurrences, current_index = 0, 0

while current_index != -1:
    current_index = text.find(lookup_text, current_index)
    print(current_index)
    if current_index != -1:
        occurrences += 1
        current_index += 1

print(occurrences)
# ABDCCDC
# CDC