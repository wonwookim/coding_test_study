# 시간: 36ms, 메모리: 32412KB

# N : 사람의 수
# Pi : 각 사람이 돈을 인출하는데 걸리는 시간

# 접근
#     1. 사람들의 돈을 인출하는데 걸리는 시간을 오름차순으로 정렬
#     2. 각 사람의 돈을 인출하는데 걸리는 시간을 누적합으로 계산
#     3. 누적합을 모두 더하여 총 시간을 계산
import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int,input().split()))

p.sort() # 그리디 접근을 위함

waiting_time = 0
total_time = 0

for p_i in p:
    waiting_time += p_i
    total_time += waiting_time

print(total_time)