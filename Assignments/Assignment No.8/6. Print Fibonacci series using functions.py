# 6. Print Fibonacci series using functions

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(b, end=" ")
        a, b = b, a + b


n = int(input("Enter number of terms: "))
fibonacci(n)