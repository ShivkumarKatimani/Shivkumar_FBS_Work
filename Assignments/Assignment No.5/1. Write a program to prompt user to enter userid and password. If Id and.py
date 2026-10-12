# 1. Write a program to prompt user to enter userid and password. If Id and  

correct_id = "admin"
correct_password = "1234"

for i in range(3):

    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid User ID or Password")

else:
    print("3 attempts completed. Program terminated.")