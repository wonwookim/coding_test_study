## 메모리 : 33432 KB, 시간 : 56ms

import sys
N = int(sys.stdin.readline())

prices = list(map(int, sys.stdin.readline().strip().split()))

M = int(input())

max_price = 0
total = 0

for price in prices :
  total += price

# 총합이 M보다 작으면 리스트의 최대값이 정답이 됨됨
if total <= M :
  max_price = max(prices)
else :
  left = 0
  right = max(prices)

  while left <= right :
    mid = (left + right) // 2
    total = 0
    for price in prices :
      if price < mid :
        total += price
      elif price >= mid :
        total += mid

    if total <=  M :
      max_price = mid
      left = mid + 1

    elif total > M :
      right = mid - 1

print(max_price)    

