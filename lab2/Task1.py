import math

down = int(input("Enter down limit: "))
up = int(input("Enter upper limit: "))
x = int(input("Enter X: "))
sum = 0
while down <= up:
    sum += (pow(-1,down)*pow(x,down))/math.factorial(down)
    down = down + 1

print("Sum of series: ", sum)
