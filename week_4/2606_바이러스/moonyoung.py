## 메모리 : 32412KB, 시간 : 32ms
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
stack = []

for _ in range(M) :
    first, second = map(int, sys.stdin.readline().split())
    graph[first].append(second)
    graph[second].append(first)


def virus(node) :
    visited = [False] * (N + 1)
    count = 0
    stack = [node]
    while len(stack) > 0 :
        node = stack.pop()
        if visited[node] == False :
            visited[node] = True
            count += 1
            for n in graph[node] :
                if visited[n] == False :
                    stack.append(n)
    return count - 1

print(virus(1))