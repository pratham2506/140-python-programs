def find_even_nums(num):
    return [ x for x in range(1,num+1) if x % 2 == 0]
print(find_even_nums(8))