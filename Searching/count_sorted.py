# Q: Count element in sorted array in O(logn)
# S: Binary search the first and last occurence and subtract them to get result

A = [10, 20, 20, 30, 30, 30, 40, 50, 60, 70]

def first_occr(A, elem):

    low, high = 0, len(A) - 1

    while (low <= high):
        mid = low + (high - low) // 2

        if elem < A[mid]:
            high = mid - 1
        elif elem > A[mid]:
            low = mid + 1
        else:
            if mid == 0 or A[mid] != A[mid - 1]: 
                return mid
            high = mid - 1 # We are searching binarily instead of linear search

    return -1

def last_occr(A, elem):
    n = len(A)
    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if elem < A[mid]:
            high = mid - 1
        elif elem > A[mid]:
            low = mid + 1
        else:
            if mid == n - 1 or A[mid+1] != A[mid]:
                return mid
            low = mid + 1
    
    return -1

def count_sorted(A, elem):

    first = first_occr(A, elem)
    if first == -1:
        print(-1)
    print(last_occr(A, elem) - first + 1)

count_sorted(A, 70)



