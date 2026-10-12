start = int (input("enter start : "))
end = int (input("enter end  : "))

for num in range (start, end + 1 ):
    if num % 7 == 0 and num % 5 ==0:
        print(num)