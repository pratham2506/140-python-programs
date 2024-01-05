#first way
# arr = [1,2,3,4,5]
# ans = sum(arr)
# print("Sum of the array is ",ans)


#second way
def sum_of_array(arr):
    total = 0
    for element in arr:
        total += element
    return total
array = [1,2,3,4,5]
result = sum_of_array(array)
print("The sum of array is ",result)