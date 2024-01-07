import re
def check_special_char(in_str):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
    if re.search(pattern,in_str):
        return True
    else:
        return False
input_string = str(input("Enter the string : "))
contains_special = check_special_char(input_string)
if contains_special:
    print("There are special characters in the string.")
else:
    print("There are no special characters in the string.")
    