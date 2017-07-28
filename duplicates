import random

randomList = []
duplicates = []

for i in range(6):
    randomList.append(random.randint(0,15))

print(randomList)

if len(randomList) != len(set(randomList)):
    for num in set(randomList):
        if randomList.count(num) > 1:
            duplicates.append(num)
    print("DUPLICATES: " + str(duplicates))
else:
    print("YAY! NO DUPLICATES!")
