userInput = input('Battery level:')
batteryLevel = int(userInput)

if batteryLevel >= 80:
    print('電量充足')
elif batteryLevel < 80 and batteryLevel >= 20:
    print('電量穩定輸出中')
else:
    print('快要沒電啦')
