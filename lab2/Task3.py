numbers = input("Enter 6 random numbers using comma: ")
array = numbers.split(',')
print(array[3])
print(array[::-1])
sum = 0

for item in array:
    sum = sum + int(item)

print("Sum: ", sum)
print("Average: ", sum/6)