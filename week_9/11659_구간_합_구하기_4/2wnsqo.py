# 41144KB	236ms
import sys

N, M = map(int, sys.stdin.readline().strip().split()) # N 수의 개수 M 합을 구애햐 하는 횟수
nums = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * (N+1)
s = 0
for i in range(N): # 누적합 계산 
    s += nums[i]
    dp[i+1] = s

for _ in range(M): # 누적합 - 시작점까지의 합 
    start, end = map(int, sys.stdin.readline().strip().split())
    print(dp[end]-dp[start-1])