def check_special_number():
    num = int(input("Enter a 3 digit number: "))

    first = num // 100
    second = (num // 10) % 10
    third = num % 10

    if first == 2 * second and third == 2 * first:
        print("Yes, you have done it")
    else:
        print("Please try next time")


check_special_number()