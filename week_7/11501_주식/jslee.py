import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))
    
    max_price = 0
    total_profit = 0

    for price in reversed(stock):
        if price > max_price:
            max_price = price
        else:
            total_profit += max_price - price

    print(total_profit)
