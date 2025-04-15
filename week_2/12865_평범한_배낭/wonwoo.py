import sys

input = sys.stdin.readlines()

N, k = map(int,input[0].strip().split())
weight_value = [list(map(int, line.split())) for line in input[1:]]
print(weight_value)

w_dp = {0:0} # weight dp table
v_dp = {0:0} # value dp table

for i in range(1, len(weight_value)): # 상향식
    if v_dp[i-1] + weight_value[i][1] <= k: # 이전 부피가 최대 부피보다 작을 떄
         # i번째 부피 
        # 이전 부피 + 현재 부피 더했을 때 최대 값
        w_dp[i] = w_dp[i - 1] + weight_value[i][0]
        v_dp[i] = v_dp[i-1] + weight_value[i][1]
    else:
        w_dp[i] = w_dp[i - 1]
        v_dp[i] = v_dp[i - 1]

print(w_dp)