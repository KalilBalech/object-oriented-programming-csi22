def removeEmptyTuples(tupleList):
    newList = []
    for tuple in tupleList:
        if len(tuple) == 0:
            newList.append(tuple)
    for tuple in newList:
        tupleList.remove(tuple)


# tuple_list = [(1, 0), (0, 1), (7, 8), (), (1, 1), (0, 0)]
# print(tuple_list)
# removeEmptyTuples(tuple_list)
# print(tuple_list)

