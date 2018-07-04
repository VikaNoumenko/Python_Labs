string = input("Enter string")
print(len(string))
array = string.split(' ')
print("Quantity of words ",len(array))

minWord = array[0]
maxWord = array[0]

for word in array:
    if len(word) > len(maxWord):
        maxWord = word
    if len(word) < len(minWord):
        minWord = word

print("Maximum length: ", len(maxWord))
print("Minimum length:", len(minWord))

newString = string.replace('*', '')
print(newString)

newNewString = ""

for char in newString:
    newNewString = newNewString + char*2

print(newNewString)
