a = int(input("Enter a: "))

total = 0

for i in range(1, 11):

    total += (a ** i) / i

print("Sum =", total)