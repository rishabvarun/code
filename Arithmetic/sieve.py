def isPrime(n):
    if n == 1: return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i or n % (i + 2):
            return False
        i += 6
    return True

P = [True for i in range(101)]

def sieve_of_eras(n):
    i = 2
    while i*i <= n:
        if isPrime(i):
            j = i*i
            while j <= n:
                P[j] = False
                j += i
        i += 1

def printPrimes(n):
    sieve_of_eras(n)
    for i in range(2, n):
        if P[i]:
            print(i, end=' ')

printPrimes(100)


