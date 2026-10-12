#3. Pascal'tringle

for i in range (5):
    num = 1

    for j in range(5-i):
        print(" ",end= " ")

    for j in range( i+1):
        print(num,end = " ")
        num =  num * (i -j )// ( j+1)
    print()