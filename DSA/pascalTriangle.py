"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""
def pascalTriangle(input_num):
    pascal_list = []
    pascal_list.append([1])
    for i in range(input_num-1):
        newRow = [1]
        for j in range(i):
            newRow.append(pascal_list[i][j] + pascal_list[i][j + 1])
        newRow.append(1)
        pascal_list.append(newRow)
    return pascal_list

print(pascalTriangle(4))



def generatePascal(numRows):
    pascalTriangle = [[1] * x for x in range(1, numRows + 1)]
    for row in range(2, len(pascalTriangle)):
        for col in range(1, row):
            pascalTriangle[row][col] = pascalTriangle[row - 1][col] + pascalTriangle[row - 1][col - 1]
    return pascalTriangle

print(generatePascal(4))