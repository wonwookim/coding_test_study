# 57628	504

import sys

input_ = sys.stdin.readline
str1 = input_().strip()
str2 = input_().strip()
N, M = len(str1) + 1, len(str2) + 1
dp = [[0] * M for _ in range(N)]

for i in range(1, N):
    s1 = str1[i - 1]
    for j in range(1, M):
        s2 = str2[j - 1]
        if s1 == s2:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[N - 1][M - 1])

