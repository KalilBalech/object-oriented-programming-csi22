def sumNumList(numList):
    sumList = 0
    for num in numList:
        sumList += num
    return sumList

def rowSum(matrix):
    return list(map(sumNumList, matrix))

#print(rowSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))