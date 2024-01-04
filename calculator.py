def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def divide(x,y):
    return x / y
def mutli(x,y):
    return x * y
print("Select operation")
print("1. Addition")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")
while(True):
    choice = input("Select option (1/2/3/4) : ")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))
        if choice == '1':
            print(num1, "+" ,num2, "=" ,add(num1,num2))
        elif choice == '2':
            print(num1, "-" ,num2, "=" ,sub(num1,num2))
        elif choice == '3':
            print(num1, "/" ,num2, "=" ,divide(num1,num2))
        elif choice == '4':
            print(num1, "*" ,num2, "=" ,mutli(num1,num2))
        next_calculation = input("Let's do more crunching? (yes/no) : ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")

