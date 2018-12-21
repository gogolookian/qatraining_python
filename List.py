a = [10,30,50,70,90]
theSumOfTheScores = 0
theRevisedSumOfTheScores = 0

for i in range(0, len(a)):
    print(a[i])
    theSumOfTheScores += a[i]

theAverageOfTheScores = theSumOfTheScores / len(a)
print(theAverageOfTheScores)

b = []
for j in range(0, len(a)):
    b.append(a[j]**0.5*10)
    print([b[j]])
    theRevisedSumOfTheScores += b[j]

theRevisedAverageOfTheScores = theRevisedSumOfTheScores / len(b)
print(theRevisedAverageOfTheScores)

print(a[:])
print(b[:])