import random

theAnswer = random.randint(1, 100)

for i in range(0,10):
    userInput = input('1-100之內，猜個數字吧')
    theNumberUserGuesses = int(userInput)
    if theNumberUserGuesses == theAnswer:
        print('Bingo!')
        break
    elif theNumberUserGuesses <= theAnswer:
        print('太小了，再猜一次看看')
    else:
        print('太大了，再猜一次看看')
