def rec(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

first = int(input("First number: "))
second = int(input("Second number: "))


print(rec(first,second))