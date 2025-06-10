#시간 44ms 메모리 32412KB
import sys
input = sys.stdin.readline

N = int(input().strip())
# 시간이 작은 순서대로 정렬
times = sorted(list(map(int,(input().split()))))

answer = []
for i in range(N):
    answer.append(sum(times[:i+1]))
print(sum(answer))

# 작은 시간을 먼저 처리하면 총합이 줄어든다 = 그리디 알고리즘
# 앞사람의 인출시간이 뒤 사람에게 그대로 누적되므로, 
# 작은 시간부터 처리하는 것이 전체 대기 시간의 합을 최소화한다