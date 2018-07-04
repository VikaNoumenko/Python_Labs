number = float(input("Enter number: "))
hundreds = number // 100
rem = number % 100
number = rem * 10 + hundreds
print("The number is: %d" % number)