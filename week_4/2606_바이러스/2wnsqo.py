# 32456KB	32ms
import sys
N = int(sys.stdin.readline().strip())
T = int(sys.stdin.readline().strip())
graph = {}
for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split(' '))
    if graph.get(a): # 이렇게 해야한다
        graph[a].append(b)
    else:
        graph[a] = [b]

    if graph.get(b): # 이렇게 해야한다
        graph[b].append(a)
    else:
        graph[b] = [a]

visited = [False] * (N+1)
listt = []
def virus(graph,start,visited, list):
    if visited[start] == False:
        visited[start] = True
        if graph.get(start): # 이렇게 해야한다
            list.extend(graph[start])
        if len(list)>=1:
            virus(graph,list.pop(),visited, list)
        else:
            return
    else: # visited[start] == True
        if len(list)>=1:
            virus(graph,list.pop(),visited, list)
        else:
            return

virus(graph,1,visited, listt)
print(sum(visited)-1)