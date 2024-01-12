def square_digits(n):
    num_str = str(n)
    result_str = ""
    for digit in num_str:
        square_digits = int(digit) ** 2
        result_str += str(square_digits)
    return int(result_str)
print(square_digits(9119))