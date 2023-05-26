def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

def fib_itr(n):
    if n==1 or n==0:
        return  n
    a = 0
    b = 1
    c = 1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
       
    return c

print(fib_itr(10), fib(10))  
