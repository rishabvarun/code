A = [0, 2, 3, 0, 5, 0, 10, 0, 0, 1]

def zeroes_to_end(A):

    c = 0 # Count of non zero elements
    i, n = 0, len(A)

    while i < n:
        if A[i] != 0:
            A[i], A[c] = A[c], A[i] # Swap every non zero element with pos of last zero
            c += 1 # Increment count of non zero element
        i += 1

    return A

A = zeroes_to_end(A)
print(A)