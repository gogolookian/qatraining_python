import string
import random
 
def verifyIdNumber(idString):

    if len(idString) != 10:
        print("長度不對! 這是假的!")
    elif verifyFirstLetter(idString[0]) == False:
        print("第一碼根本不是大寫英文字母! 這是假的!")
    else:
        idList = list(idString)
        idNumberList = []
        
        dictLettersToNumbers = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":34,"J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,"Q":24,"R":25,"S":26,"T":27,"U":28,"V":29,"W":32,"X":30,"Y":31,"Z":33}
        a = dictLettersToNumbers[idList[0]]
        idNumberList.append(a)

        for j in range(1,10):
            idNumberList.append(int(idList[j]))
            # print(idNumberList)
        x = idNumberList[0] // 10
        y = idNumberList[0] % 10
        
        sum = x * 1 + y * 9 + idNumberList[1] * 8 + idNumberList[2] * 7 + idNumberList[3] * 6 + idNumberList[4] * 5 + idNumberList[5] * 4 + idNumberList[6] * 3 + idNumberList[7] * 2 + idNumberList[8] * 1
        verificationNumber = (10 - (sum % 10))%10

        if idNumberList[9] == verificationNumber and (idNumberList[1] == 1 or idNumberList[1] == 2):
            print("身分證無誤")
        else:
            print("這是假的!")


def verifyFirstLetter(stringFirstLetter):
    returnValue = False

    firstLetter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(0,26):
        if stringFirstLetter == firstLetter[i]:
            returnValue = True
            break
    return returnValue

if __name__ == "__main__":
    verifyIdNumber(input("輸入身分證字號："))