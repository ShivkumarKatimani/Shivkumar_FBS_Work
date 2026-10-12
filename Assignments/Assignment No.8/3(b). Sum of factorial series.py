# 3(b). Sum of factorial series

def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


def factorial_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + factorial(i)

    return total


n = int(input("Enter n: "))
print("Sum of factorial series:", factorial_series(n))