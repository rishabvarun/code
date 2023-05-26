import sys

A = [-3, 8, -2, 4, -5, 6]
# *** IMPORTANT *** 
# we can get all sub arrays in n^2 time
# A[i,j] i 0-->n j i+1-->n 

# Kadane's algo: In order to solve in O(n)
# We first need max_ending including i, this means max_end always including elemnt i
# if prev max_end is positive (no matter how small) it will increase the cur max_end value
# If an array has [ -1, -1, 100, -1, -1, 50, -1, -1]
# We cannot just consider 100 and 50 we need to consider the 2 -1's in between also as it is subarray
# A max sub_seq would be sum of all +ve elements
# **We need to either include the prev element 100% or not include anything prev**
# When we compute max_end for 50 we can add 98
# max_ending(i) = max (max_ending(i-1) + A[i], A[i]) 
# Any of the max_ending's can be the final result as in this case after coming across 50
# we can only add -1s which will decrease the res so future max_ends wont be the result

def max_subarray(A):

    res = A[0]
    max_end = A[0] # max subarray initially will be the first element
    for i in range(1, len(A)):
        max_end = max(A[i], max_end + A[i])
        res = max(max_end, res)
    print(res)

max_subarray(A)

# *** Kadane's algorithm ***
# Almost same as prev just that if anytime max_end becomes less than 0
# we set max_end as 0 as no point including the prev subarray

def Kadane(A):
    maxSum = - sys.maxsize
    maxEndingHere = 0
    for x in A:
        maxEndingHere = maxEndingHere + x

        if maxEndingHere > maxSum:
            maxSum = maxEndingHere

        if maxEndingHere < 0:
            maxEndingHere = 0
        
    print(maxSum)

Kadane(A)
