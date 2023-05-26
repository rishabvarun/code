#Q: Eq point is the index of arr where sum of elements in left and right of point are same
 
A =[1, 2, 3, 100, 6]

def equilibrium(A):
    ls, rs = 0, sum(A) # Initial values

    for i in range(len(A)):
        rs -= A[i]      # We shouldn't include that element in lsum or rsum
        if ls == rs:    # for i=0 we need to consider lsum as 0 and for i=n-1 we need rsum to be 0
            print(A[i], i)
            return
        ls += A[i]
    
    print(-1)

equilibrium(A)

