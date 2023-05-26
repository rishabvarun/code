def knapsack(wt, val, W, n):
    if n==0 or W==0:
        return 0
    elif n==1:
        return val[n]
    elif (wt[n-1] <= W):
        return max (val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
    else:
        return knapsack(wt, val, W, n-1)        

def knapsack_DP(wt, val, W, n):
    DP = [ [0] * (W + 1) for x in range(n + 1) ] 
    
    for i in range(n+1):
        for j in range(W+1):
            print(i,j)
            if i==0 or j==0:
                DP[i][j] = 0
            elif wt[i] <= j:
                DP[i][j] = max(val[i] + DP[i-1][j-wt[i]], DP[i-1][j])
            else:
                DP[i][j] = DP[i-1][j]
    
    print (DP[n][W])

W = [20, 30, 40, 15]
V = [18, 25, 35, 12]
maxW = 60

profit = knapsack(W, V, maxW, 4)
print(profit)
knapsack_DP(W, V, maxW, 4)
