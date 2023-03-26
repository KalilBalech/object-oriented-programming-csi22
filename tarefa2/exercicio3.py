def possuiAlfa(str):
    for char in str:
        if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
            return True
    return False

def possuiNum(str):
    for char in str:
        if (ord(char) >= 48 and ord(char) <= 57):
            return True
    return False

def possuiTudo(strList):
    newList = []
    for str in strList:
        if(possuiAlfa(str) and possuiNum(str)):
            newList.append(str)
    return newList

#firstList = ["lçks1dfjg", "@#¨&*a$0%¨&*", "$%¨&*5%¨&Z*()", "$%¨&*(9a---)", "????0?", "$%¨&¨%$#$%Z&¨$%"]
#print(possuiTudo(firstList))