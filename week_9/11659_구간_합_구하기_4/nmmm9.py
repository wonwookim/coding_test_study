# 41144	236ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 계산
result = [0] * (n + 1)
for i in range(1, n+1):
    result[i] = result[i-1] + arr[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(result[j] - result[i-1])
