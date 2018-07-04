import random

i = 0
n = 50
list = []
while i < n:
    list.append(random.randint(-5, 5))
    i = i+1

print(list)

newList = []
nullList = []

for item in list:
    if item != 0:
        newList.append(item)
    else:
        nullList.append(item)


maximum = newList[0]

for item in list:
    if item > maximum:
        maximum = item

maxIndex = newList.index(maximum)

for item in nullList:
    newList.insert(maxIndex+1, item)

print(newList)

