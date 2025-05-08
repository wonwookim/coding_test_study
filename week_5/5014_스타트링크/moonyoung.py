# 메모리 : 41796 KB, 시간 : 604 ms
from collections import deque
import sys
F, S, G, U, D = map(int, sys.stdin.readline().split())

if S == G :
  print(0)
  exit()

queue = deque()
queue.append((S,0))

visited = [False] * (F + 1)
visited[S] = True

while queue :
  current, count = queue.popleft()

  if current == G :
    print(count)
    break
  
  # 위로 이동
  up = current + U
  if up <= F and visited[up] == False :
    visited[up] = True
    queue.append((up, count+1))

  # 아래로 이동
  down = current - D
  if down >= 1 and visited[down] == False :
    visited[down] = True
    queue.append((down, count + 1))
else :
  print('use the stairs')