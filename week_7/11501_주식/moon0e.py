## 메모리 : 134888 KB, 시간 : 2216ms

import sys
T = int(sys.stdin.readline())

for _ in range(T) :
    prices = []
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().strip().split()))
    
    def max_profit(prices) :
        total_profit = 0
        max_price = 0

        for i in reversed(range(len(prices))) :
            if prices[i] < max_price : # 현재 주가가 최댓값보다 작으면 주식을 사고
                total_profit += (max_price - prices[i])
            else : # 현재 주가가 크면 최댓값 업데이트
                max_price = prices[i]
        return total_profit
    
    print(max_profit(prices))   