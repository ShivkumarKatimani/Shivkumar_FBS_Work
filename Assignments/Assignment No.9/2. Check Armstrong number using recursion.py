def armstrong_sum(num, digits):
    if num == 0:
        return 0

    digit = num % 10
    return digit ** digits + armstrong_sum(num // 10, digits)


def is_armstrong(num):
    if num < 0:
        return False

    digits = len(str(num))
    return armstrong_sum(num, digits) == num


n = int(input("Enter a number: "))

if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")