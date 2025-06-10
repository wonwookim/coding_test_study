# 시간: 32ms, 메모리: 32412KB

# T: test case
# test case n은 11보다 작은 양수

# 접근 (dp)
    # |    n    |  경우의 수
    # |    1    |     1개
    # |    2    |     2개
    # |    3    |     4개         -->  점화식 : f(n) = f(n - 3) + f(n - 2) + f(n - 1)
    # |    4    |     7개
    # |    5    |    13개
    # |    6    |    24개

import sys
input = sys.stdin.readline

T = int(input())

# dp 초기 설정
dp = {1 : 1, 2: 2, 3: 4}

for _ in range(T):
    num = int(input())

    for i in range(1, num + 1):
        if dp.get(i, -1) == -1:
            dp[i] = dp[i -3] + dp[i - 2] + dp[i - 1]
    
    print(dp[num])
