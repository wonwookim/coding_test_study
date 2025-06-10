#시간 40ms, 메모리 32544KB
import sys
input = sys.stdin.readline

N = int(input().strip())

if N == 1:
    print(1) # dp[1] = 1
elif N == 2:
    print(2) # dp[2] = 2
else:
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,N+1):
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[N]%10007)
