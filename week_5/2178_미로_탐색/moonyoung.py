# 메모리 : 34936 KB, 시간 : 76 ms
# 최단거리를 구해야 하므로 BFS 사용
from collections import deque
N, M = map(int, input().split())
maze = []
for _ in range(N) :
  maze_input = input()
  maze_line = list(map(int, maze_input))
  maze.append(maze_line)

queue = deque()
queue.append((0,0)) # 시작위치 넣어둬야함

# 이동 방향 만들기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue : 
  x, y = queue.popleft()
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M :
      if maze[nx][ny] == 1 :
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))
print(maze[N-1][M-1])# 메모리 : 34936 KB, 시간 : 76 ms
# 최단거리를 구해야 하므로 BFS 사용
from collections import deque
N, M = map(int, input().split())
maze = []
for _ in range(N) :
  maze_input = input()
  maze_line = list(map(int, maze_input))
  maze.append(maze_line)

queue = deque()
queue.append((0,0)) # 시작위치 넣어둬야함

# 이동 방향 만들기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue : 
  x, y = queue.popleft()
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M :
      if maze[nx][ny] == 1 :
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))
print(maze[N-1][M-1])