def find_one_odd(arr):
    res = 0
    for x in arr:
        res ^= x
    return res

def find_two_odd(arr):   
    xor = 0
    for x in arr:
        xor ^= x
    set_bit = xor & ~(xor - 1) # Gives the rightmost set bit, Since xor is 1 
    res1, res2 = 0, 0          # this means that that this bit is set in either one of the two numbers
    for x in arr:              # Now divide the array into 2 sets one in which this bit is set
        if x & set_bit:
            res1 ^= x
        else:
            res2 ^= x
    print(res1, res2)

find_two_odd([1,2,1,1,2,1,3,4,5,5,4,6])
