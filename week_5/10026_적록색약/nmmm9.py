import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

# 이동 방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y, visited, graph, is_weak):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    current_color = graph[x][y]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                next_color = graph[nx][ny]

                # 적록색약이라면 R과 G를 같은 색으로 취급
                if is_weak:
                    if (current_color in 'RG' and next_color in 'RG') or current_color == next_color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    if next_color == current_color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

# 구역 세기 함수
def count_areas(is_weak):
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, visited, graph, is_weak)
                count += 1
    return count

# 일반인
normal_count = count_areas(False)
# 적록색약
color_weak_count = count_areas(True)

print(normal_count, color_weak_count)
