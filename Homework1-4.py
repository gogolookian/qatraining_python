def printer(number):
    for i in range(0,number):
        for j in range(0,number-i-1):
            print(' ',end='')
        for k in range(0,(i*2)+1):
            print('*',end='')
        print('')
    for a in range(0,number-1):
        for b in range(0,a+1):
            print(' ',end='')
        for c in range(0,number*2-a*2-3):
            print('*',end='')    
        print('')

if __name__ == "__main__":
    a = input('請輸入一個整數：')
    b = int(a)
    printer(b)
