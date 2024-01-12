def mean(n):
    n_str = str(n)
    digit_sum = sum(int(digit) for digit in n_str)
    digit_count = len(n_str)
    digit_mean = digit_sum / digit_count
    return int(digit_mean)
print(mean(12345))