def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev


def palindrome(num):
    return num == reverse_number(num)


n = int(input("Enter a number: "))

if palindrome(n):
    print("Palindrome number")
else:
    print("Not a palindrome number")