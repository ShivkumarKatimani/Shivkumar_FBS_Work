def series_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))
print("Sum of series:", series_sum(n))