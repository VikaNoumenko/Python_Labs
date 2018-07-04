import random

list =[]
i = 0
n = 20
while i < n:
    list.append(random.randint(-10,2))
    i = i+1

print(list)

minimum = list[0]


for item in list:
    if item < minimum:
        minimum = item

minIndex = list.index(minimum)
currentIndex = minIndex+1

while currentIndex < len(list) - 1:
    if list[currentIndex] < 0:
        list.pop(currentIndex)
    else:
        break

print(list)