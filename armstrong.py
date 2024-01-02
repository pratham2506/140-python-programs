num = int(input("Enter the number : "))
num_str = str(num)
num_digit = len(num_str)
sum_of_power = 0
temp_num = num
while temp_num > 0:
    digit = temp_num % 10
    sum_of_power += digit ** num_digit
    temp_num //= 10
if sum_of_power == num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")
    