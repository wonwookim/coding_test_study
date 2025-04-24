import sys

N = int(input())
M = int(input())

visited = [False] * (N+1) # 1번부터 시작하니 전부 N+1
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(graph, next, visited)


dfs(graph, 1, visited)

total_infected_computer = sum(visited) - 1 #1번 제외
print(total_infected_computer)

