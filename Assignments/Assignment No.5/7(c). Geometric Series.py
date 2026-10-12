n = int(input("Enter n: "))

total = 0

for i in range(n):
    total += 2 ** i

print("Sum =", total)