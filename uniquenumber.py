def unique(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] +=1 
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        if count == 1:
            return num
print(unique([3, 3, 3, 7, 3, 3]))