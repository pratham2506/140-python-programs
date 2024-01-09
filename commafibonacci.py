def comma_fibonacci(n):
    sequence = [0,1]
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2,n)]
    return sequence
try:
    n = int(input("Enter a value for n : "))
    result = comma_fibonacci(n)
    print(','.join(map(str,result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")