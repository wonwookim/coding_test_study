import sys
from collections import deque

N, M, V = map(int, input().split())
visited_dfs = [False] * (N+1) 
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start, visited):
    for neighbors in graph:
        neighbors.sort()
    visited_dfs[start] = True
    print(start, end=' ')
    for next in graph[start]:
        if not visited_dfs[next]:
            dfs(graph, next, visited)

def bfs(graph, start):
    for neighbors in graph:
        neighbors.sort()
    visited_bfs = [False] * (N+1)
    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next in graph[node]:
            if not visited_bfs[next]:
                queue.append(next)
                visited_bfs[next] = True




dfs(graph, V, visited_dfs)
print()
bfs(graph, V)
