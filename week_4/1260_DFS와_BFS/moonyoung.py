## 메모리 : 35572KB, 시간 : 72ms
import sys
from collections import deque

N, M, V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
# 0번째 리스트는 쓰지 않기 위해 N + 1
# 이유는 밑에서 입력받을 때 graph[0]은 없을 것이기 때문에
for i in range(M) :
    X, Y = map(int, sys.stdin.readline().split())
    # 양방향이어야 하기 때문에 x-y 서로 입력
    graph[X].append(Y)
    graph[Y].append(X)

visited = [False] * (N + 1)

def DFS(node) :
  stack = [node]

  while len(stack) > 0 :
    node = stack.pop()
    if visited[node] == False :
      visited[node] = True
      print(node, end=' ')
      for n in sorted(graph[node], reverse = True) :
        if visited[n] == False :
          stack.append(n)

visited_queue = [False] * (N + 1)

def BFS(node) :
  queue = deque([node])

  while len(queue) > 0 :
    node = queue.popleft()
    if visited_queue[node] == False :
      visited_queue[node] = True
      print(node, end=' ')
      for n in sorted(graph[node]) :
        if visited_queue[n] == False :
          queue.append(n)  


DFS(V)
print("")
BFS(V)