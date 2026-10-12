def armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    return total == original


n = int(input("Enter a number: "))

if armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")