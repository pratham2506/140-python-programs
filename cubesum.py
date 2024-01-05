def cube_sum_natural_number(n):
    if n <= 0:
        return 0
    else:
        total = sum([i ** 3 for i in range(1,n+1)])
        return total
n = int(input("Enter the number : "))
if n <= 0:
    print("Please enter a positive number")
else:
    result = cube_sum_natural_number(n)
    print(f"The sum of the first {n} natural numbers is {result}")