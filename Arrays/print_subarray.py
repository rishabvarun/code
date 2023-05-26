A = [1, 2, 3, 4, 5]
n = len(A)

def print_subarr(A, start=0, end=0):

    if start > end:
        print_subarr(A, 0, end+1)
        return
    
    if end == n:
        return
    
    print(A[start:end+1])
    print_subarr(A, start + 1, end)
    
print_subarr(A)