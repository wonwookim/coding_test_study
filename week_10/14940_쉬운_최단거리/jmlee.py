#시간 748ms, 메모리 41608KB

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]

dist = [[-1]*M for _ in range(N)]

# 상하좌우 이동 벡터
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 시작 위치 찾기
for i in range(N):
    for j in range(M):
        if grid[i][j] == 2:
            start_x, start_y = i, j
            dist[i][j] = 0  # 시작점은 거리 0

queue = deque()
queue.append((start_x, start_y))

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 경계 조건 & 갈 수 있는 칸(1) & 방문 안한 곳만 탐색
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

#모든 칸에 대해 dfs 호출 후 출력
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()