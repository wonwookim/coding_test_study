# 40224KB	556ms
import sys

N = int(sys.stdin.readline().strip())

dp = [0] * (N+1)

if N >= 2:
    dp[2] = 1
if N >=3:
    dp[3] = 1

if N >=4: # 경우의 수 모두 구한 후 최소값 넣기 
    for i in range(4,N+1):
        min_num = []
        if i % 2 == 0:
            min_num.append(dp[i//2] +1)
        if i % 3 == 0:
            min_num.append(dp[i//3] +1)
        min_num.append(dp[i-1] +1)

        dp[i] = min(min_num)

print(dp[N])