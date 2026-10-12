n = int(input("enter a three - digit num:"))

a = n // 100
b = (n // 10) % 10
c = n % 10

sum = a + b + c

print("sum",sum)