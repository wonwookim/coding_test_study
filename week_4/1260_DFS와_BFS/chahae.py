# 35580	68
# 첫째줄 정점의 개수N, 간선의 개수 M, 시작할 정점 V
# 양방향......이였다 / 작은수부터였다 ㅠㅠㅠ
from collections import deque
import sys
input_ = sys.stdin.readline

N, M, V = map(int, input_().split())

graph = {}
for _ in range(M):
    P, C = map(int, input_().split())
    if P not in graph:
        graph[P] = []
    if C not in graph:
        graph[C] = []
    graph[P].append(C)
    graph[C].append(P)
        
        
def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        p = stack.pop()
        if p not in visited:
            visited.add(p)
            print(p, end=' ')
            
            if p in graph:
                for c in reversed(sorted(graph[p])):
                    if c not in visited:
                        stack.append(c)
                    

def bfs(graph, start):
    visited = set([start]) 
    queue = deque([start])
    
    while queue:
        p = queue.popleft()
        print(p, end = ' ')
        
        if p in graph:
            for c in sorted(graph[p]):
                if c not in visited:
                    visited.add(c)
                    queue.append(c)
    
    

dfs(graph, V)
print()
bfs(graph, V)
    