def prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0: # Optional optimisation i*i <= n should be enough
            return False                   # and increment i by 1
        i += 6 # Based on the principle every prime num can be written of the form 6n +/- 1
    return True

def print_primes_opt(n):
    if n < 2: return
    if n < 3:
        print(2)
        return
    print(2,3,end =' ')
    i = 5
    while i < n:
        if (prime(i)):
            print(i,end=' ')
        if (prime(i+2)):
            print(i+2,end=' ')
        i += 6

def print_primes(n):
   for i in range(2,n+1):
        if prime(i):
            print(i,end=' ')

print_primes(100)
