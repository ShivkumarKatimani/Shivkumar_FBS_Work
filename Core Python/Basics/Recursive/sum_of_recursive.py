def sumOfseries(n):
    if(n <=0):
       return 0
    else:
        return n + sumOfseries(n - 1 )
    
n = 5 
res = sumOfseries(n)
print(res)