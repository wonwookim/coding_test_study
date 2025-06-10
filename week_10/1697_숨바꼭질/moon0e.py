## 메모리 : 36608 KB, 시간 : 104 ms

import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

visited = [False] * 100001

queue = deque()
visited[N] = True
queue.append((N,0)) 

def BFS(current) :
  
  while len(queue) > 0 :
    current, time = queue.popleft()

    if current == K :
      print(time)
      return 

    move = [current-1, current+1, current*2]
    
    for next_pos in move :
      if 0 <= next_pos <= 100000 and not visited[next_pos]:
        visited[next_pos] = True
        queue.append((next_pos, time + 1))


BFS(N)