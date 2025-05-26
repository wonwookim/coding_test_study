#시간 32ms, 메모리 32412KB
import sys
input = sys.stdin.readline

# 1차 시도: 재귀+딕셔너리 -> 누적되지 않음
# return은 숫자 리턴용이라 호출횟수를 셀 수 없어서 fibonacci()를 호출해도 아무 출력이 없다
# 2차 시도: N의 범위가 40까지밖에 안되므로 DP로 미리 계산해두고 출력

T = int(input().strip())
testcase = [int(input().strip()) for _ in range(T)]

dp = [[0,0] for _ in range(41)]
dp[0] = [1,0] #fibonacci(0)
dp[1] = [0,1] #fibonacci(1)

for i in range(2,41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for n in testcase:
    print(dp[n][0], dp[n][1])


# answer = {'0':0, '1':1}
# def fibonacci(n):
#     if (n==0):
#         answer['0'] += 1
#     elif (n==1):
#         answer['1'] += 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#     return ' '.join(answer.values())

# for i in houses:
#     fibonacci(i)
    