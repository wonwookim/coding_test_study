# 시간: 44ms, 메모리: 32412KB

# 접근 방법: 
#    점화식
#      - f(n)을 2×n 직사각형을 채우는 방법의 수라 하면,  
#      - 맨 왼쪽에 2×1 타일을 세로로 하나 놓으면 나머지는 f(n-1)
#      - 맨 왼쪽에 1×2 타일 두 개를 가로로 놓으면 나머지는 f(n-2)  
#           f(1) = 1,
#           f(2) = 2
#           f(n) = f(n-1) + f(n-2) (n >= 3)
#     
#   초기값 설정
#      - 배열 dp를 크기 n+1로 선언  
#      - dp[1] = 1, dp[2] = 2
#      - 점화식을 적용하며 매 연산마다 10007로 나머지 처리


import sys
input = sys.stdin.readline
n = int(input().strip())

dp = [0] * (n + 1)


MOD = 10007

def dp_fun(n):
    
    if n == 1:
        print(1)
        return
    
    dp[1], dp[2] = 1, 2 # n = 1일 경우를 방지하기 위해 n== 1 밑에 작성
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    print(dp[n])

dp_fun(n)
