# Q: Find an element in a sorted array by dividing it into 3 parts

A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def ternary_search(A, elem):

    l, r = 0, len(A) - 1
    
    while l <= r:
        mid1 = l + (r - l) // 2
        mid2 = r - (r - l) // 2

        if A[mid1] == elem:
            print(mid1); return
        elif A[mid2] == elem:
            print(mid2); return

        if elem < A[mid1]:
            r = mid1 - 1
        elif elem > A[mid2]:
            l = mid2 + 1
        else:
            l, r = mid1 + 1, mid2 - 1
    
    print(-1)

ternary_search(A, 20)