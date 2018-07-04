import math

Radius1 = float(input("Enter the length of radius R1: "))
Radius2 = float(input("Enter the length of radius R2: "))

Square1 = math.pi*(Radius1**2)
print("Square of 1st circle: S1 = %.2f " % Square1)

Square2 = math.pi*(Radius2**2)
print("Square of 2nd circle:: S2 = %.2f " % Square2)

Square3 = Square2 - Square1
print("Hoop circle equals to: S3 = %.2f " % Square3)