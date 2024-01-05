def largest_element_in_array(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]
    for element in arr:
        if element > largest_element:
            largest_element = element
    return largest_element
my_array = [1,2,3,4,5]
result = largest_element_in_array(my_array)
print("The largest element of array is ",result)