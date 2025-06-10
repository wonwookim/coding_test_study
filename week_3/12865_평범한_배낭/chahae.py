# 281576	3912
import sys

input_ = sys.stdin.readline
N, K = map(int, input_().split())
bag = [tuple(map(int, input_().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = bag[i - 1]
    for j in range(1, K + 1):
        if j >= w:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])