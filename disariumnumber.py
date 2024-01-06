def is_desarium(number):
    num_str = str(number)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return digit_sum == number
try:
    num = int(input("Enter a number :"))
    if is_desarium(num):
        print(f"{num} is a Disarium number")
    else:
        print(f"{num} is not a Disarium number")
except ValueError:
    print("Invalid input. Please enter a valid input.")