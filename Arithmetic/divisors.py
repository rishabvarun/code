def divisors(n): # Prints in ascending order, can print //n if you want random order
    i = 1
    while i*i <= n:
        if n % i == 0:
            print(i, end=' ')
        i += 1
    i -= 1
    while i >= 1:
        if n % i == 0:
            print (n//i, end=' ')
        i -= 1

divisors(60) 


