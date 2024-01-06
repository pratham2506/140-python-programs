def is_desarium(num):
    num_str = str(num)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate (num_str))
    return num == digit_sum
disarium_numbers = [num for num in range(1,1001) if is_desarium(num)]
print("Disarium numbers between 1 to 1000 :")
for num in disarium_numbers:
    print(num,end='|')