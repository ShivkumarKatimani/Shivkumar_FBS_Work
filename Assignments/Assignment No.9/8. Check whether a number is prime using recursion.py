def check_prime(num, divisor):
    if num < 2:
        return False

    if divisor == num:
        return True

    if num % divisor == 0:
        return False

    return check_prime(num, divisor + 1)


n = int(input("Enter a number: "))

if check_prime(n, 2):
    print("Prime number")
else:
    print("Not a prime number")