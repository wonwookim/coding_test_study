# N: 수빈이가 있는 위치, M: 동생이 있는 위치 (0 ≤ N & M ≤ 100,000)
# 접근
    # DP사용 -> X
        # f(n) = min((f(n-1) + 1), (f(n + 1) + 1), (f(n/2) + 1)) (N<= n <= M)
    
    # DFS
        # graph를 -1, +1, //2를 얻기
        # + 1 하는 방식으로 진행
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = {i: [i-1, i+1, i * 2] for i in range(M) if i > 0}
print(graph)

# dp = [1e7] * (M  + 2)
# dp[N] = 0
# for i in range(N+ 1, M + 1): # M까지의 값을 다 구하기
#     print(i)
#     dp[i] = min(dp[i-1], dp[i + 1], dp[i//2]) + 1

# print(dp[M])

    
