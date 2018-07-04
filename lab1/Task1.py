import math

a = float(input("Cathetus a = "))
b = float(input("Cathethus b = "))

c = math.sqrt(a**2 + b**2)
print("Hypotenuse C = %.2f" % c)

P = a + b + c
print("Perimeter P = %.2f" % P)