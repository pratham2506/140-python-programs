def missing_num(lst):
    total_sum = sum(range(1,11))
    given_sum = sum(lst)
    missing = total_sum - given_sum
    return missing
print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))