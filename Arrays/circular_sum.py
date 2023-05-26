# Q: Find the max sum of circular subarray
# A: A circular subarray will include all subarrays where you can start from any 
# element and end at prev element

import sys
A = [8, -3, 2, 1, -5, 7]

# Naive method O(n^2) Compute all circular subarray sums
def circular_sum(A):
    n = len(A)
    _max = - sys.maxsize
    for i in range(n):
        _sum = 0
        for j in range(1, n):
            index = (i+j) % n # Each circular subarray is like subarray when you consider A[i] as starting element
            _sum += A[index]
            if _sum > _max:
                _max = _sum
    print(_max)

circular_sum(A)

# Optimal method: 
# 1) Use Kadane's algo to find min subarray sum (min subarray sum is same as max subarray sum when you complement all elements)
# 2) Max circular sum = Total array sum - min subarray sum
# This works because when we do a max circular subarray sum only the minimum subarray (should be -ve)
# which has least value will be left behind (rest all elements will be considered no matter how small)

def Kadane(A):
    maxEndHere = 0
    _max = - sys.maxsize
    for x in A:
        maxEndHere += x
        if maxEndHere > _max:
            _max = maxEndHere
        if maxEndHere < 0:
            maxEndHere = 0
    return _max

def solution(A):
    normalMaxSubarraySum = Kadane(A) 
    if normalMaxSubarraySum < 0: # This is must and required only for handling case where all arr elements are -ve
        return normalMaxSubarraySum # If this case is not handled then the func will return 0 when all arr elements are -ve

    totalSum = 0
    for i in range(len(A)):
        totalSum += A[i]
        A[i] = -A[i] # Complement all elements for min subarray sum
    
    minSubarraySum = Kadane(A)
    if minSubarraySum < 0: #Imp not seen in video
        minSubarraySum = 0
    circularSubarrySum = totalSum + minSubarraySum # Since we have complemented all elements we add here instead of subtracting
    return circularSubarrySum
A = [1, 2, 3, 4]
print(solution(A))


