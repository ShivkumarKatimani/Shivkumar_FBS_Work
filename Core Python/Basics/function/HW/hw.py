# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False

#     return True


# num = int(input("Enter number: "))

# print(is_prime(num))

################# Palindrome number

# def is_palindrome(num):
#     original = num
#     reverse = 0

#     while num > 0:
#         digit = num % 10
#         reverse = reverse * 10 + digit
#         num = num // 10

#     return original == reverse


# num = int(input("Enter number: "))

# print(is_palindrome(num))


#############Strong Number


# def is_strong(num):
#     original = num
#     total = 0

#     while num > 0:
#         digit = num % 10

#         fact = 1
#         for i in range(1, digit + 1):
#             fact = fact * i

#         total = total + fact
#         num = num // 10

#     return original == total


# num = int(input("Enter number: "))

# print(is_strong(num))


# ######### Armstrong Number

# def is_armstrong(num):
#     original = num
#     digits = len(str(num))
#     total = 0

#     while num > 0:
#         digit = num % 10
#         total = total + digit ** digits
#         num = num // 10

#     return original == total


# num = int(input("Enter number: "))

# print(is_armstrong(num))


# ############## Perfect Number

# def is_perfect(num):
#     total = 0

#     for i in range(1, num):
#         if num % i == 0:
#             total = total + i

#     return total == num


# num = int(input("Enter number: "))

# print(is_perfect(num))


def count(n):
    if n > 0:
        print(n)
        count(n - 1)

count(5)
print(type(count))