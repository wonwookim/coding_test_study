#시간 104ms 메모리 42784KB
import sys
lines = [list(map(int,line.strip().split())) for line in sys.stdin.readlines()]
n, m, v = lines[0] #n, m, v = 4, 5, 1
edges = lines[1:]
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

#graph는 dict, start는 시작 정점, v는 정점, visited는 리스트
#스택(LIFO)
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
    for neighbor in sorted(graph.get(start, [])):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

#큐(FIFO)
import queue
def bfs(graph,start):
    visited = {start}
    bfs_queue = queue.Queue()
    bfs_queue.put(start)
    while not bfs_queue.empty():
        v = bfs_queue.get()
        print(v, end=' ')
        for neighbor in sorted(graph.get(v, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                bfs_queue.put(neighbor)

dfs(graph,v,set())
print()
bfs(graph,v)