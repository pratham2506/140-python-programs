def is_triplet(a,b,c):
    sorted_number = sorted([a,b,c])
    return sorted_number[0] ** 2 + sorted_number[1] ** 2 == sorted_number[2] **2
print(is_triplet(13, 5, 12))