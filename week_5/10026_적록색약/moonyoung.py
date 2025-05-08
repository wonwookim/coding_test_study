# 메모리 : 35044 KB, 시간 : 68ms 
from collections import deque
import sys
N = int(sys.stdin.readline())
image = []
for i in range(N) :
  image_input = sys.stdin.readline()
  image.append(list(image_input))

visited = [[False]*N for _ in range(N)]
visited_color = [[False]*N for _ in range(N)]
dx = [-1, 1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우

def bfs(x, y, color) :
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  while queue :
    x, y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N :
        if visited[nx][ny] == False and image[nx][ny] == color :
          visited[nx][ny] = True
          queue.append((nx, ny)) 

def bfs_color(x, y, color) :
  queue = deque()
  queue.append((x, y))
  visited_color[x][y] = True
  while queue :
    x, y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N :
        if visited_color[nx][ny] == False :
          if color in['R', 'G'] and image[nx][ny] in ['R', 'G'] :
            visited_color[nx][ny] = True
            queue.append((nx, ny))
          elif image[nx][ny] == color :
            visited_color[nx][ny] = True
            queue.append((nx, ny))
count = 0
count_color = 0
for i in range(N) :
  for j in range(N) :
    if visited[i][j] == False :
      bfs(i, j, image[i][j])
      count += 1
    if visited_color[i][j] == False :
      bfs_color(i, j, image[i][j])
      count_color += 1
print(count, count_color)
