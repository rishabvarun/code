def ToH(n, start, end, pivot):
    if n==1:
        print('Move disc 1 from {} to {}'.format(start, end))
        return
    ToH(n-1, start, pivot, end)
    print('Move disc {} from {} to {}'.format(n, start, end))
    ToH(n-1, pivot, end, start)

ToH(3, 'A', 'C', 'B')