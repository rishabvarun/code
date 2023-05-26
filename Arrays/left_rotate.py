#P: Left rotate array by d spaces without using extra space
#A: Here we reverse first d and last d elements and reverse whole array at end
#Note: We can solve the problem with d extra space easily

A = [1, 2, 3, 4, 5, 6]

def reverse(A):
    low = 0
    high = len(A) - 1

    while low < high:
        A[low], A[high] = A[high], A[low]
        low += 1
        high -= 1

    return A

def left_rotate(A, d):

    A[:d] = A[:d][::-1] # A[:d] = reverse(A[:d])
    A[d:] = A[d:][::-1] # A[d:] = reverse(A[d:])
    A = A[::-1] # A = reverse(A)
    print(A)

left_rotate(A, 2)


