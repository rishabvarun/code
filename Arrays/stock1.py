# Max profit with unlimited transactions

A = [10, 20, 30, 20, 50, 40, 60, 70]

def max_profit(price, n):
    profit = 0
    for i in range(1, n):
        if price[i] > price[i-1]:  # We are doing some of all crests
            profit += price[i] - price[i-1]
    print(profit)

max_profit(A, len(A))
    

