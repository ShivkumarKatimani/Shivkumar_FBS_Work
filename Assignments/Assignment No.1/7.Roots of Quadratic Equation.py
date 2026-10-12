import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)

    print("Root 1 =", x1)
    print("Root 2 =", x2)

elif d == 0:
    x = -b / (2*a)
    print("Both roots are =", x)

else:
    print("No real roots")