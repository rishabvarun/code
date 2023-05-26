def gcd_rec(a, b):
    if a==b:
        return a
    elif a > b:
        return gcd(b, a - b)
    else:
        return gcd(a, b - a)

def gcd(a, b):
    while(a != b):
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def gcd_opt(a, b):
    if a % b == 0: # or same as if b == 0 return a 
        return b
    else:
        return gcd_opt(b, a % b)

def my_gcd(a, b):
    
    while a != 0 and b!= 0:      
        if a > b:
            temp = b
            b = a % b
            a = temp
        else:
            temp = a
            a = b % a
            b = temp
    return b if a == 0 else a
            

print(gcd_opt(16,420), my_gcd(16,420))

    