def filter_list(lst):
    result = []
    for element in lst:
        if isinstance(element,int) and element >= 0:
            result.append(element)
    return result
print(filter_list([1, 2, "a", "b"]))