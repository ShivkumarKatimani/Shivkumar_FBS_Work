#num =  int ( input("enter the num : "))
#for i in range (2 ,num):
#    if ( num % i  == 0 ) :
#        print(f'{num} is not a prime num.')
#        break
#else:
#    print(f'{num}is a prime num ')

#n = int( input("enter the num : "))
#for num in range(2, n + 1):
#   for i in range(2, num):
#       if(num % i == 0):
#          break
#   else:
#       print(num,end =' ')      

#wap to print first n prime num 

n = int(input("Enter n: "))

count = 0
num = 2

while count < n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        count += 1

    num += 1