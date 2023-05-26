def my_pow(x,n):

    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2:
        return my_pow(x, n//2) * my_pow(x, n//2) * x
    else:
        return my_pow(x, n//2) * my_pow(x, n//2)

dp = [-1 for i in range(100)]

def my_powDP(x, n):

    if n == 0: return 1
    if n == 1: return x

    if n % 2:
        if dp[n//2] != -1:
            return dp[n//2] * dp[n//2] * x
        else:
            dp[n//2] = my_powDP(x, n//2)
            return dp[n//2] * dp[n//2] * x
    else:
        if dp[n//2] != -1:
            return dp[n//2] * dp[n//2] 
        else:
            dp[n//2] = my_powDP(x, n//2) 
            return dp[n//2] * dp[n//2] 


def pow(x, n):
    if n == 0:
        return 1
    tmp = pow(x, n//2) # Divide the problem
    tmp = tmp * tmp # Conquer the problem
    if n % 2 == 0:
        return tmp
    else:
        return tmp * x

def pow_opt(x, n):
    res = 1
    while(n > 0):
        if (n & 1): # last bit is 1 same as % 2 ==1 OPTIMAL
            res = res * x # value of x will be x^1 , x^2, x^4 ...
        x = x * x
        n = n >> 1 # Same as n divided by 2 OPTIMAL
    return res
