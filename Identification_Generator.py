import string
import random

def idGenerator():

    idNumberList = []
    firstLetter = random.choice(string.ascii_uppercase)
    idNumberList.append(firstLetter)
    secondNumber = random.randint(1,2)
    idNumberList.append(secondNumber)

    for i in range(0,7):
        a = random.randint(0,9)
        idNumberList.append(a)
    
    return idNumberList

def addLastCheckNumber(idNumberList):
    # print(idNumberList)
    dictLettersToNumbers = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":34,"J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,"Q":24,"R":25,"S":26,"T":27,"U":28,"V":29,"W":32,"X":30,"Y":31,"Z":33}
    a = dictLettersToNumbers[idNumberList[0]]
    x = a // 10
    y = a % 10
    # print(a, x, y)

    sum = x * 1 + y * 9 + idNumberList[1] * 8 + idNumberList[2] * 7 + idNumberList[3] * 6 + idNumberList[4] * 5 + idNumberList[5] * 4 + idNumberList[6] * 3 + idNumberList[7] * 2 + idNumberList[8] * 1
    lastCheckNumber = 10 - (sum % 10)
    if lastCheckNumber == 10:
        idNumberList.append(0)
    else: 
        idNumberList.append(lastCheckNumber)

    # print(idNumberList)
    return idNumberList

def printId(idNumberList):
    
    for i in range(0,10):
        print(idNumberList[i], end='')
    print('')

if __name__ == "__main__":
    printId(addLastCheckNumber(idGenerator()))
    
    
