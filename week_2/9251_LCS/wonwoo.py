# 2차원 dp: 시간: 1708ms 메모리: 135816KB
# 1차원 dp: 시간 : 200ms 메모리: 32412KB
import sys
input = sys.stdin.readline

str_1 = input().strip()
str_2 = input().strip()

# def lcs_solve(str_1, str_2):
#     dp = {'-1_-1': 0}
#     dp.update({str(a)+ '_-1' : 0 for a in range(len(str_1))})
#     dp.update({'-1_'+ str(a) : 0 for a in range(len(str_2))}) # padding처럼 배열 맨 앞에 0으로 채워넣기
#     for i in range(len(str_1)):
#         for j in range(len(str_2)):
#             current = str(i)+ '_' +str(j)
#             prev_i = str(i - 1) + '_' + str(j)
#             prev_j = str(i) + '_' + str(j - 1)
#             prev_ij = str(i - 1) + '_' + str(j - 1)
#             if str_1[i] == str_2[j]:
#                 dp[current] = dp[prev_ij] + 1
#             else:
#                 dp[current] = max(dp[prev_i], dp[prev_j])
#     return max(list(dp.values()))
# print(lcs_solve(str_1, str_2))


# 1차원 dp
dp = [0] * len(str_2)
for i in range(len(str_1)):
    start = 0
    for j in range(len(str_2)):
        if start < dp[j]:
            start = dp[j]
        elif str_1[i] == str_2[j]:
            dp[j] = start + 1
print(max(dp))