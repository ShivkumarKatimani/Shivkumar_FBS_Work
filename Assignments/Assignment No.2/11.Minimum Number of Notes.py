amount = int (input("enter amount :"))

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount=amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

print("n500",n500)
print("n200",n200)
print("n100",n100)
print("n50",n50)
print("n20",n20)
print("n10",n10)