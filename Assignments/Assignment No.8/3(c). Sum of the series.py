def power_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i ** i

    return total


n = int(input("Enter n: "))
print("Sum of power series:", power_series(n))