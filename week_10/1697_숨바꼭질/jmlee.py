#시간 96ms, 메모리 38780KB
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
time = 0

# 최단거리 : BFS
visited = [False] * 100001
dist = [0] * 100001

def bfs(x,y):
    queue = deque([x])
    visited[x] = True
    while queue:
        node = queue.popleft()
        if node == y:
            return dist[y]
        for nx in [node-1, node+1, node*2]:
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                dist[nx] = dist[node] + 1
                queue.append(nx)
        
print(bfs(N,K))