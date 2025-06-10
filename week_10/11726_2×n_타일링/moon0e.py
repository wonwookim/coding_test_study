## 메모리 : 32544 KB, 시간 : 36 ms

# 마지막에 타일 세로로 놓으면 앞은 dp[n-1]의 값
# 마지막에 타일 가로로 놓으면 앞은 dp[n-2]의 값

import sys
N = int(sys.stdin.readline())
dp = []

def tile(N) :
    if N == 1 :
        return 1
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1) :
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

print(tile(N) % 10007)

## 시간 44 ms

# def tile(N) :
#     dp = [0] * (N+1)
#     dp[1] = 1
#     if N >= 2 :
#         dp[2] = 2
#         for i in range(3, N+1) :
#             dp[i] = dp[i-1] + dp[i-2]
#     return dp[N]

# print(tile(N)%10007)