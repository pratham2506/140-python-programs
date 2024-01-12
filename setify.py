def setify(lst):
    unique_set = set(sorted(lst))
    return list(unique_set)
print(setify([1, 3, 3, 5, 5]))