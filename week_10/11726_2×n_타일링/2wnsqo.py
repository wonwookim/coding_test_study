# 32544KB	48ms
# 누적합이랑 똑같다
import sys

n = int(sys.stdin.readline().strip())

dp = [0] * (n+1)


if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] # 점화식

    print(dp[n]%10007)
