# 시간: 340ms, 메모리: 32412KB

# N : 정수의 개수, S : 더했을 때, 목표 값
# 접근:
    # 백트레킹을 이용
        # 정렬
        # 그래서 for 구문으로 다음 값을 확인을 하며 그 값이 목표 값보다 크면 x
        
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
visited = [False] * (N + 1)

def backtracking(idx, total):
    global result
    if total == S and idx != -1:
        # print(a)
        result += 1
    if idx == N:
        return
    # print(f'추가된 배열열{a}')
    # print(idx)
    for i in range(idx + 1, N):
        if not visited[i]:
            visited[i] = True
            backtracking(i, total + arr[i])
            visited[i] = False
    
backtracking(-1, 0)

print(result)

