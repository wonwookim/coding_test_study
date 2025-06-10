# 32412KB	32ms
import sys

T = int(sys.stdin.readline().strip()) # 테스트 케이스 

for _ in range(T):
    N = int(sys.stdin.readline().strip()) # 숫자 
    dp = [(0,0)] * (N+1)
    
    if N >= 2:
        dp[0] = (1,0)
        dp[1] = (0,1)
        for i in range(2,N+1):
            dp[i] = (dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1])
        print(dp[N][0],dp[N][1])


    elif N == 0:
        print('1 0')
    elif N == 1:
        print('0 1')

    