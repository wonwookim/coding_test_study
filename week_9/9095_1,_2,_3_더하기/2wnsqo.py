# 32412KB	32ms
import sys

T = int(sys.stdin.readline().strip())

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,12): # 1+a 2+b 3+c 로 쪼갠 후 dp적용
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(dp[n])