def count_occerance(l,element):
    count = l.count(element)
    return count
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
element_to_count = 2
occurances = count_occerance(my_list,element_to_count)
print(f"The element {element_to_count} appears {occurances} times in the list.")
