n = int(input("Enter n: "))

fact = 1
total = 0

for i in range(1, n + 1):

    fact = fact * i
    total = total + fact

print("Sum =", total)