## 메모리 : 70108 KB, 시간 : 792 ms

import sys
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M) :
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

def DFS(node) :
    stack = [node]

    while len(stack) > 0 :
        current = stack.pop()
        if visited[current] == False :
            visited[current] = True
            for n in graph[current] :
                if visited[n] == False :
                    stack.append(n)

count = 0
for i in range(1, N+1) :
    if visited[i] == False :
        DFS(i)
        count += 1
print(count)