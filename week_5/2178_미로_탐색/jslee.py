# 메모리: 34976KB, 시간: 72ms


import sys
from collections import deque

N, M = map(int, input().split())

# 1부터 시작하기 위한 위한 패딩
maze = [[0] * (M + 1)]
for _ in range(N):
    maze.append([0] + list(map(int, input().strip())))

def bfs_maze(graph, start_X, start_Y):
    visited_bfs = [[False] * (M+1) for _ in range(N+1)]
    distance = [[0] * (M+1) for _ in range(N+1)]
    queue = deque([(start_X, start_Y)])
    visited_bfs[start_X][start_Y] = True
    distance[start_X][start_Y] = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= M:
                if not visited_bfs[nx][ny] and graph[nx][ny] == 1:
                    visited_bfs[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    print(distance[N][M])

bfs_maze(maze, 1, 1)
