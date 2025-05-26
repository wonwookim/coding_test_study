#시간 552ms, 메모리 40660KB
#처음에 재귀로 풀었다가 리턴하고 매번 다시 전달받는게 비효율적이라 판단
#DP로 점화식 세우기.. 바텁업

import sys
input = sys.stdin.readline
N = int(input().strip())

dp = [0 for _ in range(N+1)]

dp[1] = 0

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1 # 기본연산: 1을 빼는 경우 (2나 3의 배수가 아닐때)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: # 2와 3 둘다 배수인 경우를 고려해서 elif 말고 if로 처리
        dp[i] = min(dp[i],dp[i//3] + 1)

print(dp[N])