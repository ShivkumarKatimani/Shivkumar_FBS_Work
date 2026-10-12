def check_leap_year():
    year = int(input("Enter a year: "))
 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("NOT a Leap year")
        else:
            print("Leap Year")
    else:
        print("NOT a Leap year")

check_leap_year()