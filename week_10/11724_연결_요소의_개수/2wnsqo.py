# 75252KB	888ms
import sys
inputs = sys.stdin.readline

N, M = map(int, inputs().split()) # 정점의 개수, 간선의 개수
visited = [False] * (N+1)
graph = {}

count =0
for _ in range(M):
    a, b = map(int, inputs().split())
    if graph.get(a):
        graph[a].append(b)
    else:
        graph[a] = [b]

    if graph.get(b):
        graph[b].append(a)
    else:
        graph[b] = [a]

for i in range(1,N+1):
    if visited[i] == False:
        visited[i] = True
        dots = []
        if graph.get(i):
            dots.extend(graph[i])
            while dots:
                dot = dots.pop()
                if visited[dot] == False:
                    visited[dot] = True
                    if graph.get(dot):
                        dots.extend(graph[dot])
            count += 1
        else:
            count +=1

print(count)
