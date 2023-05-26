# Find the max diff max(A[j] - A[i]), j > i
# Note if the array is sorted in reverse order then ans should be least negative difference

A = [2, 3, 10, 6, 4, 8, 1]

def func(A):
    _min = A[0]
    res = A[1] - A[0]
    for i in range(1, len(A)):
        res = max(A[i] - _min, res)
        _min = min(A[i], _min)
        
    print(res)

func(A)

