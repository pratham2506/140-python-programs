def recurrsion_factorial(n):
    if n == 1:
        return n
    else:
        return n*recurrsion_factorial(n-1)
num = int(input("Enter the number : "))
if num < 0:
    print("Sorry, factorial of negative number does'nt exist")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recurrsion_factorial(num))