#4.Valid Triangle. Otherwise → Invalid Triangle.

a = int (input ("enter side 1 : "))
b = int (input ("enter side 2 : "))
c = int (input ("enter side 3 : "))

if a + b > c and b + c > c and a + c > b :
    print("valid triangle")
else:
    print("invalid triangle")

    