def list_operation(x,y,n):
    return [num for num in range(x,y+1) if num % n == 0]
print(list_operation(1, 10, 3))