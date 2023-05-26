# Q: Element is majority if it occurs more than n/2 times
# Return index of majority element (index of any occurence of it)

# Moore's voting algo: 2 steps
# 1) Find a candidate
# 2) Check if candidate is majority

A = [8, 4, 3, 8, 1, 8, 8]


def solution(A):
    candidate = 0 # Let index 0 be candidate 
    c, n = 1, len(A)
    for i in range(1, n):
        if A[i] == A[candidate]:
            c += 1
        else:
            c -= 1
        if c == 0:
            candidate = i # This will be new candidate
            c = 1  
    
    # If there is a majority element it should be the candidate
    # But it is not certain that it is the majority

    if A.count(A[candidate]) > n // 2:
        return A[candidate]
    else:
        return -1

print(solution(A))