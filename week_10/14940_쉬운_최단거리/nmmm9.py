# 41668	728
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]  # 기본값 -1로 초기화

# 목표지점 찾기 (2인 곳)
for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            start = (y, x)
        if graph[y][x] == 0:
            dist[y][x] = 0  # 갈 수 없는 땅은 0으로 고정

# BFS 시작
q = deque()
q.append(start)
dist[start[0]][start[1]] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))

# 결과 출력
for row in dist:
    print(*row)
