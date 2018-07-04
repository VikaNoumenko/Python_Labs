number = float(input("Enter number: "))
hundreds = number // 100
ten = number % 100 // 10
units = number % 10
number = units * 100 + ten * 10 + hundreds
print("Gotten number: %d" % number)