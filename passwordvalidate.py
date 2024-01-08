import re
def is_valid(password):
    if 6 <= len(password) <= 12:
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])",password):
            return True
    return False
passwords = input("Enter passwords separated by commas : ").split(',')
valis_passwords = []
for pws in passwords:
    if is_valid(pws):
        valis_passwords.append(pws)
print(",".join(valis_passwords))