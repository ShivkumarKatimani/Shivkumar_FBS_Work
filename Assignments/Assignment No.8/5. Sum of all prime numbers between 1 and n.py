# 5. Sum of all prime numbers between 1 and n

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_sum(n):
    total = 0

    for i in range(2, n + 1):
        if is_prime(i):
            total = total + i

    return total


n = int(input("Enter n: "))
print("Sum of prime numbers:", prime_sum(n))