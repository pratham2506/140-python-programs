def even_number(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num
try:
    n = int(input("Enter a value for n : "))
    result = even_number(n)
    print(','.join(map(str,result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
    