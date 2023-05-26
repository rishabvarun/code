#Q: Find sum from index i to j
#Q: Find weighted sum from i to j --> A[i] + 2*A[i+1] + 3*A[i+2]...  

A = [1, 2, 3, 4, 5, 6]

def preprocess1(A): # Prefix Sum
    prefixSum = [0 for i in range(len(A))]
    prefixSum[0] = A[0]
    for i in range(1, len(A)):
        prefixSum[i] = prefixSum[i-1] + A[i]
    return prefixSum

def preprocess2(A): # Prefix weighted sum
    prefixSum = [0 for i in range(len(A))]
    prefixSum[0] = A[0]
    for i in range(1, len(A)):
        prefixSum[i] = prefixSum[i-1] + (i+1) * A[i]
    return prefixSum

def sol1(A, i, j):
    preprocess = preprocess1(A) # In actual implementation, need to do it only once 
    if i == 0:
        print(preprocess[j]); return
    print(preprocess[j] - preprocess[i-1])

# If you expand this in paper you will find ans
# We need to right this in terms of summation A[i]
# To compute,
# summation i: l --> r | (i - l + 1) * A[i] // Very imp we write in terms of A[i]
# Expand this we get
# summation i: l --> r | i * A[i] - (l - 1) * summation i: l --> r | A[i]
# To compute this we need weighted sum and normal sum prefix array

def sol2(A, i, j): # Weighted sum
    prefix1 = preprocess1(A)
    prefix2 = preprocess2(A)
    if i == 0:
        print(prefix2[j]); return
    res = (prefix2[j] - prefix2[i-1]) - i * (prefix1[j] - prefix1[i-1]) # Here we are multiplying by i and not i - 1 because in the theoretical summation numbering starts from 1 and in the weighted sum we need to start multiplying from 1
    print(prefix2[j] - prefix2[i-1])
    print(res)
    
sol2(A, 2, 5)




