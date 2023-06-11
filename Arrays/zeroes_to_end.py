A = [0, 2, 3, 0, 5, 0, 10, 0, 0, 1]

def zeroes_to_end_swap(A):

    c = 0 # Count of non zero elements
    i, n = 0, len(A)

    while i < n:
        if A[i] != 0:
            A[i], A[c] = A[c], A[i] # Swap every non zero element with pos of last zero
            c += 1 # Increment count of non zero element
        i += 1

    return A

def zeroes_to_end_count(arr):
    
    non_zero = 0
    i, n = 0, len(arr)
    
    while i < n:
        if arr[i] != 0:
            arr[non_zero] = arr[i]
            non_zero += 1
        i += 1
    
    for i in range(non_zero + 1, n):
        arr[i] = 0
        
    return arr
                      
A = zeroes_to_end_swap(A)
print(A)
A = zeroes_to_end_count(A)
print(A)
