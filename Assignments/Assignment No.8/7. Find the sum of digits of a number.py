def sum_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total


n = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(abs(n)))