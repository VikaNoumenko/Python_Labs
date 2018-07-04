number = float(input("Enter number: "))
hundreds = number // 100
tens = number % 100 // 10
units = number % 10
sum = hundreds + tens + units
productNumbers = hundreds * tens * units
print("Sum of digits in number: %.2f" % sum)
print("Multiplication of number of digits in number: %.2f" % productNumbers)