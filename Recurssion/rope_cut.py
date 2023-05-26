# Cab cut the rope into pieces of len of only a, b, or c
# Find the max number of cuts that can be made

def max_cuts(n, a, b, c):

    if n < 0: # Cannot cut the rope to this piece
        return -1 
    if n == 0: # This is a possible solution
        return 0
    res = max(max_cuts(n - a, a, b, c), max_cuts(n - b, a, b, c), max_cuts(n - c, a, b, c))

    if res == -1: # Entire sequence should return false
        return -1
                   # Once you return 0 it always leads to a solution we just need to compute how
    return res + 1 # many recurssive calls we made in this path


print(max_cuts(14, 3, 4, 5)) # O(3^n)