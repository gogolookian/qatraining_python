firstInputValue = input('第一個數')
inputSymbol = input('加減乘除')

if inputSymbol != '+' and inputSymbol != '-' and inputSymbol != '*' and inputSymbol != '/':
    print('這樣人家怎麼算啦~')

secondInputValue = input('第二個數')

firstValue = int(firstInputValue)
symbol = inputSymbol
secondValue = int(secondInputValue)

if symbol == '+':
    print(firstValue + secondValue)
elif symbol == '-':
    print(firstValue - secondValue)
elif symbol == '*':
    print(firstValue * secondValue)
else:
    print(firstValue / secondValue)