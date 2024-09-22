import math
a = int(input("first number "))
b = int(input("second number "))
c = input("Operation ")
d = a + b
if c == "*" or c == "Multiply":
    print(a*b)
elif c == "/" or c == "Divide":
    print(a/b)
elif c == "-" or c == "substract":
    print(a-b)
elif c == "floor":
    print(a//b)
elif c == "square root":
    e = math.sqrt(d)
    print(e)
else:
    print(a+b)
