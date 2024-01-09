def extract_email(email):
    parts = email.split('@')
    if len(parts) == 2:
        return parts[0]
    else:
        return "Invalid email address"
try:
    email = input("Enter an email address: ")
    username = extract_email(email)
    print(username)
except ValueError:
    print("Invalid input. Please enter a valid email address.")
