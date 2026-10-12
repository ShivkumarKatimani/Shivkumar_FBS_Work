def count_digits(num):
    if num == 0:
        return 0

    return 1 + count_digits(num // 10)


def reverse_number(num, digits):
    if num == 0:
        return 0

    last_digit = num % 10
    return (last_digit * (10 ** (digits - 1))
            + reverse_number(num // 10, digits - 1))


n = int(input("Enter a number: "))

if n == 0:
    print("Reverse:", 0)
else:
    result = reverse_number(abs(n), count_digits(abs(n)))
    print("Reverse:", result)