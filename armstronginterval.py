lower = int(input("Enter the lower limit : "))
upper = int(input("Enter the upper limit : "))
for num in range(lower, upper + 1):
    order = len(str(num))
    temp_num = num
    sum = 0
    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
        if num == sum:
            print(num)