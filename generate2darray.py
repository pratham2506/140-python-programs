X,Y = map(int, input("Enter two digits : ").split(','))
array = [[0 for j in range(Y)] for i in range(X)]
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j
for row in array:
    print(row)