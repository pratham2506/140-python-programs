def remove_char(input_str,i):
    if i < 0 or i >= len(input_str):
        print(f"Invaid index {i}, the string remains unchanged")
        return input_str
    result_str = input_str[:i] + input_str[i + 1:]
    return result_str
input_str = "Hello wWorld"
i = 7
new_str = remove_char(input_str,i)
print("Original String : ",input_str)
print(f"String after removing {i}th character : {new_str}")