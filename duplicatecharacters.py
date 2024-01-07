def find_duplicate(input_str):
    char_count = {}
    duplicates = []
    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates
input_string = "Pratham Matkar"
duplicate_chars = find_duplicate(input_string)
print("Duplicate characters : ",duplicate_chars)