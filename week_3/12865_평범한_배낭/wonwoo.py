import sys

input = sys.stdin.readlines()

N, k = map(int,input[0].strip().split())
weight_value = [list(map(int, line.split())) for line in input[1:]]

w_dp = [0] * (k + 1)  # 무게 누적용 리스트
v_dp = [0] * (N + 1)  # 가치 저장용 리스트

for i in range(1, len(weight_value) + 1): # 상향식
    print(i)
    prev = k - w_dp[i]  # 이전은 전체 부피에서 현재 부피를 뺀 값이 최대임임
    conv1 = 0
    conv2 = 0
    if 0 < k: # 누적 부피가 최대 부피보다 작을 떄
        # 이전 값을 뺴고 
        conv_1= v_dp[prev] + weight_value[i - 1][1]
        # 이전 부피 + 현재 부피 더했을 때 최대 값
        w_dp[i] = w_dp[i - 1] + weight_value[i - 1][0]
    else:
        w_dp[i] = w_dp[i - 1]
        conv_2 = v_dp[i - 1]
    v_dp[i] = max(conv_1, conv_2)

print(w_dp)
print(v_dp)