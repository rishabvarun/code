# Q: Find the subarray with given sum if it exists
# A: We use sliding window technique 
# 1) Add an element and increase window if cur_sum < sum
# 2) Keep removing elements while cur_sum > sum

A = [1, 1, 1, 2, 3, 4, 4, 5, 2, 2] # All arr elements need to be +ve

def solution(A, _sum):
    cur, n = 0, len(A)
    s, e = 0, 0 # Start and end index of sliding window (subarray)
    while e < n:
        cur += A[e] # Increase sliding window
        while cur > _sum:
            cur -= A[s] # Decrease sliding window
            s += 1
        if cur == _sum:
            print('From index', s, 'to', e)
            break
        e += 1

solution(A, 9)
