
#메모리 : 41276KB, 시간: 252ms


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))


#누적합 배열
presum_list = [0] * (N + 1)
for i in range(1, N + 1): #1부터 처리해서 조건문 안 붙임
    presum_list[i] = presum_list[i - 1] + A[i - 1]


for _ in range(M):
    i, j = map(int, input().split())
    print(presum_list[j] - presum_list[i - 1])








    
