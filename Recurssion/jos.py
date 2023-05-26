# Josephus problem: In each iteration the kth person is killed
# Find the last person standing in n people (0 ... n-1)

def jos(n, k):
    if n == 1:      # When there is only one person then person 0 will be spared
        return 0
    else:
        return (jos(n - 1, k) + k) % n
print(jos(5,3))
# jos(5, 3) Here out of initial 5 people no.2 is killed
# After this we start from no.3 who becomes no.0 no.4 becomes no.1, and so on
# Here we notice that when we go from (i-1)th sub problem to ith sub problem
# the index of each element is increased by k (modulo n)
# Therefore the result of the guy spared will also increase by a factor of k at each call