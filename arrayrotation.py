def rotate_array(arr,d):
    n = len(arr)
    if d < 0 or d >= n:
        return "Invalid rotation value"
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] =arr[(i+d)%n]
    return rotated_arr
arr = [1,2,3,4,5,6,7,8,9,10]
d = 2
result = rotate_array(arr,d)
print("Original Array : ",arr)
print("Rotated Array : ",result)