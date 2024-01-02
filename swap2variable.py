#program to swap values of two variables
a=int(input("Enter the first element : "))
b=int(input("Enter the second element : "))
#display the original values
print(f"Original values of a={a}, b={b}")
#swap the value using the temporary variable
temp=a
a=b
b=temp
#display swaped values
print(f"Swaped values of a={a}, b={b}")