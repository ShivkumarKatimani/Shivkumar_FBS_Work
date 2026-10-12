import random

userid = (input("enter user id  : "))
password = (input("enter password : "))

if userid == "shiv"and password =="shiv@123":

    captcha =  random.randint(1000,9999)

    print("your captcha is",captcha)

    user_captcha = int(input(" Enter captch "))

    if user_captcha == captcha : 

        print("login successful")

    else:
        print("captcha failed")

else:
    print("invalid user id or password")


