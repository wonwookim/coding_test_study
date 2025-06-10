# 32776	40

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    graph[y][x] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                dfs(x, y)
                count += 1

    print(count)
