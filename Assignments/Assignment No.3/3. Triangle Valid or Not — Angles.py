#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a=int(input("enter first angle : "))
b=int(input("enter second angle : "))
c=int(input("enter third angle : "))

if a + b > c and b + c > a and a + c > b :
    print("vaild triangle")
else:
    print("invaild triangle")
