def simon_says(list1,list2):
    return list1[:-1] == list2[1:]
print(simon_says([1, 2], [5, 1]))