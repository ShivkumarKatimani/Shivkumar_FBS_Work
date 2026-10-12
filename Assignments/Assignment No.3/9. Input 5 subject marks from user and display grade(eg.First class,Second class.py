#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..) 

m1 = int(input("enter m1 marks : "))
m2 = int(input("enter m2 marks : "))
m3 = int(input("enter m3 marks : "))
m4 = int(input("enter m4 marks : "))
m5 = int(input("enter m5 marks : "))

total = m1 + m2 + m3 + m4 + m5

Percentage = total / 5

print("total",total)

print("percentage",Percentage)

if Percentage >= 60 : 
    print("first class")
elif Percentage >= 50 :
    print("second class")
elif  Percentage >= 35 : 
    print("pass")
else:
    print("fail")

