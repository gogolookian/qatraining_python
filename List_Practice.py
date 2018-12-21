people = []

for i in range(0,10):
    userInput = input('請輸入整數:')
    theNumberOfPeopleAttendingTheParty = int(userInput)
    people.append(theNumberOfPeopleAttendingTheParty)
    

for j in range(0,5):
    startPointOfUserInput = input('請輸入查詢開始位置')
    endPointOfUserInput = input('請輸入查詢結尾位置')
    startPointOfQuery = int(startPointOfUserInput)
    endPointOfQuery = int(endPointOfUserInput)
    print(people[startPointOfQuery:endPointOfQuery])
    print(sum(people[startPointOfQuery:endPointOfQuery]))
