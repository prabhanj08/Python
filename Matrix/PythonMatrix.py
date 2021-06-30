# Program to multiply two matrices using nested loops

# take a 3x3 matrix
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

result = [[0 for x in range(len(A))] for y in range(len(B))]

def matrix_multipliction(matrix1,matrix2):
    for i in range(len(matrix1)):
        for k in range(len(matrix2)):
            result[i][k] = matrix1[i][k] * matrix2[i][k]
    return result

def matrix_addition(matrix1,matrix2):
    for i in range(len(matrix1)):
        for k in range(len(matrix2)):
            result[i][k] = matrix1[i][k] + matrix2[i][k]
    return result



print(" Addition of Matrix A,B ")
print(matrix_addition(A,B))

print(" Multiplication of Matrix A,B")
print(matrix_multipliction(A,B))
