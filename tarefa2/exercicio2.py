def meanTuple(tupleList):

    lista = []
    for i in range (0, len(tupleList)):
        # print(tupleList[i])
        soma = 0
        for j in range (0, len(tupleList[i])):
            soma += tupleList[i][j]
            # print(tupleList[i][j])
        lista.append(int(soma/2))
    return tuple(lista)

#print(meanTuple(((1,2,3), (10,20,30), (10,20,30), (10,20,30))))