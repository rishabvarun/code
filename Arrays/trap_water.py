Block = [10, 30, 20, 50, 60, 20, 90]

def Lmax(A):
    Lmax = [0 for i in range(len(A))]
    Lmax[0] = A[0]
    for i in range(1, len(A)):
        Lmax[i] = max(A[i], Lmax[i-1])
    print(Lmax)

def solution(A):

    Lmax = [max(A[:i]) for i in range(1, len(A)+1)] # Custom func is more optimal here
    Rmax = [max(A[i:]) for i in range(len(A))]
    res = 0
    for i in range(1, len(A) - 1):  # Need to compute only for middle bars as 1st and last bar cant store
        if min(Lmax[i], Rmax[i]) - A[i] > 0: # We can ignore this condition as it will always be atleast 0 since we are considering the element also in Lmax and Rmax 
            res += min(Lmax[i], Rmax[i]) - A[i]
    print(res)

Lmax(Block)
solution(Block) 