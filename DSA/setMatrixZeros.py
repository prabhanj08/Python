"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and
column to 0's.
You must do it in place

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

def matrixZeros(matrix):
    print(len(matrix))
    ele_index = []
    for ele in range(len(matrix)):
        for val in range(len(matrix[ele])):
            if matrix[ele][val] == 0:
                ele_index.append(val)
            else:
                continue
    if ele_index:
        for ele in range(len(matrix)):
            if 0 in matrix[ele]:
                for ii in range(len(matrix[ele])):
                    matrix[ele][ii] = 0
            else:
                for _ in ele_index:
                    matrix[ele][_] = 0


    return matrix




print(matrixZeros([[1,1,1],[1,0,1],[1,1,1]]))
print(matrixZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

