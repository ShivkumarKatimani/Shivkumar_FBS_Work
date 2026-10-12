start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
given_num = int(input("Enter given number: "))

for num in range(start, end + 1):
    if num % given_num == 0:
        print(num)