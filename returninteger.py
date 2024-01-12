def return_only_integer(lst):
    return [x for x in lst if isinstance(x,int) and not isinstance(x,str)]
print(return_only_integer([9, 2, "space", "car", "lion", 16]))