def n_largest_number(lst,n):
    sorted_list = sorted(lst,reverse=True)
    largest_element = sorted_list[:n]
    return largest_element
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
N = int(input("Enter the number : "))
result = n_largest_number(numbers,N)
print(f"The {N} largest number in the list is ",result)