
n = int(input("Enter n: "))

list7 = list(range(n))
numbers = list(range(n))

for seven in list7:
    if seven%7 != 0:
        list7[list7.index(seven)] = 0

print(list7)


for number in numbers:
    if number > 1:
        for candidate in range(2 * number, len(numbers), number):
            numbers[candidate] = 0


print(numbers)

numbers2 = numbers

for number1 in numbers2:
    if number1%7!=0:
        numbers2[numbers2.index(number1)]=0

print(numbers2)