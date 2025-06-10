## 메모리 : 32412 KB, 시간 : 36ms
import sys
T = int(sys.stdin.readline())

# dp를 반복문 안에서 선언하면 N이 3이하인 경우에는 인덱스 에러가 남
# 그래서 n의 최대는 11이라고 문제에 나와있으니 12로 미리 최대치를 만들어둠 

dp = [0] * 12
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(T) :
    N = int(sys.stdin.readline())
    for i in range (4, N + 1) :
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        # 마지막에 1을 붙이는 경우 : dp[i-1]
        # 마지막에 2를 붙이는 경우 : dp[i-2]
        # 마지막에 3을 붙이는 경우 : dp[i-3]
    print(dp[N])

    