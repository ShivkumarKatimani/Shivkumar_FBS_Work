#6. Write a program to calculate profit or loss.

cp = float(input("enter cost price : "))
sp = float(input("enter selling price : "))

if sp > cp :
    profilt = sp - cp
    print("profit")

elif cp > sp:
    loss =  cp - sp
    print("loss")

else:
    print("no profit no loss")