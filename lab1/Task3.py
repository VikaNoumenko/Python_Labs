weightCandies = float(input("Enter the weight of chocolate candies: "))
rublesC = float(input("Enter sum, spent on chocolate candies: "))
weightToffees = float(input("Enter the weight of toffees: "))
rublesT = float(input("Enter sum, spent on toffees: "))

result1 = rublesC/weightCandies
print("Kilo of chocolate candies costs %.2f rubles" % result1)

result2 = rublesT/weightToffees
print("Kilo of toffees costs %.2f rubles" % result2)

res = result1/result2
print("Chocolate candies more expensive than toffees in %.2f times" % res)