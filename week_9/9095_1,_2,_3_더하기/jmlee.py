#시간 32ms, 메모리 32412KB
import sys
input = sys.stdin.readline

T = int(input().strip())
testcase = [int(input().strip()) for _ in range(T)]

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for n in testcase:
    print(dp[n])