#using slice operator
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(cloned_list)

#using list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print(cloned_list)

#using list comprehension
original_list = [1, 2, 3, 4, 5]
cloned_list = [item for item in original_list]
print(cloned_list)

