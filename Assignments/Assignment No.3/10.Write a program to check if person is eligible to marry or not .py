#10. Write a program to check if person is eligible to marry or not (male age >=21 and 
#female age>=18) 

gender = input("enter gender : ")
age = int(input(" enter age : "))

if gender == "male":
    if age >= 21:
        print("eligible to marry")
    else:
        print("not eligible to marry")

elif gender == "famale":
    if age >= 18 :
        print("eligible to marry")
    else:
        print("not eligible to marry")

else:
    print("invalid gender")