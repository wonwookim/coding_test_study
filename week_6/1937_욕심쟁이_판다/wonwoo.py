# N : 대나무 숲 크기(N x N)
# 접근:
    # graph, visited 생성
    # for 구문 이용
        # 1번째 상하좌우 확인
        # 정상 범위 내에 있을 경우 dfs 진행
        # 만약 dfs를 진행할 때, 상하좌우 값이 원래보다 크면 진행
        # 다 돌고 1번째 칸에 visited에 count만큼 추가
import sys
sys.setrecursionlimit(10**6)  # 이거 안 하면 런타임 에러 발생
input = sys.stdin.readline
N = int(input())

# 그래프, 방문 여부
graph = [list(map(int, input().strip().split()))for _ in range(N)]
visited = [[0] * N for _ in range(N)]
max_count = 0

# 상하좌우
ny = [0, 1, -1, 0]
nx = [1, 0, 0, -1]

def dfs(y, x):
    count = 1
    
    if visited[y][x] != 0: # 0이 아닌 경우 -> 이미 방문 했을 경우
        return visited[y][x]
    
    for idx in range(4): # 상하좌우 값을 확인하는 코드
        dy = y + ny[idx]
        dx = x + nx[idx]
        if 0 <= dy < N and 0 <= dx < N:
            if graph[dy][dx] > graph[y][x]: # 비교 대상이 현재 개수보다 큰 경우
                target = dfs(dy, dx)  # dfs 진행
                count = max(count, target + 1) # 더 큰 값을 가져오기기

    visited[y][x] = count
    return count

# 배열 전체 순환
for j in range(N): # y축
    for i in range(N): # x축
        max_count = max(max_count, dfs(j, i))

print(max_count)