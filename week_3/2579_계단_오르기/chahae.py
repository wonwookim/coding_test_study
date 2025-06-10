# 32412	32

import sys
input_ = sys.stdin.readline

N = int(input_())
score = [int(input_()) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

if N == 1:
    print(score[0])
elif N == 2:
    print(score[0] + score[1])
else:
    dp = [0] * N
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

    print(dp[N-1])
