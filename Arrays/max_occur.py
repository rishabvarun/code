#Q: Given two arrays having L index and R index of n ranges find the number occuring max in those ranges
# The size of L and R array is large 1 < size < 10^5, but the ranges will be always from 0 --> 100

L = [2, 7, 5, 4]
R = [10, 9, 15, 6]

def solution(L, R):
    freq = [0 for i in range(101)]

    for x, y in zip(L,R):
        freq[x] += 1 # For starting index add 1 
        freq[y+1] -= 1 # After the last index add -1

    prefix = [sum(freq[:i]) for i in range(1, 101)] # Computing prefix sum arr, Do it in O(n)
    print('Number:', prefix.index(max(prefix)), '\nCount:', max(prefix)) # Return the index of max
    
solution(L, R)
    
