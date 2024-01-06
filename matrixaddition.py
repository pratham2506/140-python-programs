def add_matrix(mat1,mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result
matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
result_matrix = add_matrix(matrix1,matrix2)
if isinstance(result_matrix,str):
    print(result_matrix)
else:
    print("Sum of matrix")
    for row in result_matrix:
        print(row)