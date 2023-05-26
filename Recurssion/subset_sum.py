# Find the number of subsets that have given sum
# Similar to subseq problem
# Decison tree method
def subset_sum(A, sum, n):
    if n == 0:
        return 1 if sum == 0 else 0
    return subset_sum(A, sum, n - 1) + subset_sum(A, sum - A[n-1], n - 1) # Two cases 
                                        # Either consider element in sum or not 

A = [10, 20, 5, 15]
sum = 30

print(subset_sum(A, sum, len(A)))