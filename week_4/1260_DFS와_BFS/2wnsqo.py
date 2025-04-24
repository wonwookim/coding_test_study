# 35004KB	388ms
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().strip().split(' '))
graph = {}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    if a not in list(graph.keys()):
        graph[a] = [b]
    else:
        graph[a].append(b)

    # 양방향 그래프 구현현
    if b not in list(graph.keys()):
        graph[b] = [a]
    else:
        graph[b].append(a)
visited = [False] * (N + 1)
list1 = []
# print(graph)
# print("------------------------------")
# 너비우선
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    if start in list(graph.keys()):
        list1 = graph[start]
        list1.sort()
        for i in list1:
            if visited[i] == False:
                dfs(graph, i, visited)

dfs(graph,V,visited)

print()

visited2 = [False] * (N + 1)
def bfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    if start in list(graph.keys()):
        listt = graph[start]
        listt.sort()
        queue = deque(listt)

        while queue:
            a = queue.popleft()
            if visited[a] == False:
                visited[a] = True
                print(a, end=' ')
                if a in list(graph.keys()):
                    listt = graph[a]
                    listt.sort()
                    queue.extend(listt)
bfs(graph,V,visited2)