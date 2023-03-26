def multMatrix(matrix1, matrix2):
    # verificar se as matrizes sao multiplicaveis
    row1 = len(matrix1)
    row2 = len(matrix2)
    column1 = len(matrix1[0])
    column2 = len(matrix2[0])

    for list in matrix1:
        if(len(list) != column1):
            return False
    if row2 != column1:
        return False
    for list in matrix2:
        if(len(list) != column2):
            return False
    
    # mulltiplicar
    matrix3 = []

    for i in range(0, row1):
        newList = []
        for j in range (0, column2):
            newList.append(0)
            for k in range(0, row2):
                newList[j] += matrix1[i][k]*matrix2[k][j]
        matrix3.append(newList)
    return matrix3




# matrix1 = [[0, 1, 2], [5, 6, 7]]
# matrix2 = [[1, 2, 3, 0], [1, 2, 3, 0], [1, 2, 3, 0]]

# print(multMatrix(matrix1, matrix2))