#32412	32

import sys
input_ = sys.stdin.readline

computer_cnt = int(input_())
N = int(input_())

graph = {}
for _ in range(N):
    P, C = map(int, input_().split())
    if P not in graph:
        graph[P] = []
    if C not in graph:
        graph[C] = []
    graph[P].append(C)
    graph[C].append(P)


def dfs(graph, start = 1):
    visited = set()
    stack = [start]

    while stack:
        p = stack.pop()
        if p not in visited:
            visited.add(p)
            if p in graph:
                for c in graph[p]:
                    if c not in visited:
                        stack.append(c)

    return len(visited)-1

print(dfs(graph))


