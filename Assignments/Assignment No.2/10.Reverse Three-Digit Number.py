n = int(input("enter a three num :"))

a = n // 100
b = (n // 10) % 10
c = n % 10

reverse = c * 100 + b * 10 + a

print("reverse",reverse)