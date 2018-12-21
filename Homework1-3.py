def printer(number):
    for i in range(0,number):
        for j in range(0,number-i-1):
            print(' ',end='')
        for k in range(0,i+1):
            print('*',end='')
        for l in range(0,i):
            print('*',end='')    
        print('')    


if __name__ == "__main__":
    a = input('請輸入一個整數：')
    b = int(a)
    printer(b)
