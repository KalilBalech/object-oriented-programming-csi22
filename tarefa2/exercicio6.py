def listConterWay(numList):
    for i in range (len(numList)-1, -1, -1):
        yield numList[i]

# for num in listConterWay([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]):
#     print(num)