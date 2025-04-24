#시간 36ms 메모리 32412KB
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
    for neighbor in sorted(graph.get(start, [])):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

import sys
lines = [list(map(int,line.strip().split())) for line in sys.stdin.readlines()]
n, m = lines[0][0],lines[1][0]
edges = lines[2:]
#list를 set로 만들기
graph = {}
for i in range(m):
    a,b = edges[i]
    # a -> b
    if a not in graph:
        graph[a] = set()
    graph[a].add(b)
    
    # b -> a (양방향)
    if b not in graph:
        graph[b] = set()
    graph[b].add(a)

virus = set()
dfs(graph,1,virus)
print(len(virus)-1) #1번을 통해 걸리는 컴퓨터의 수이므로 -1 
