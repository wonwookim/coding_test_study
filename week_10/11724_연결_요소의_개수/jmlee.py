#시간 624ms, 메모리 67048KB
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 무방향 그래프 입력 받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

count = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)     # i번 정점이 아직 연결 안 되었으면, 새로운 연결 요소!
        count += 1

print(count)
