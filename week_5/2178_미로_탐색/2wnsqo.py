# 36988KB	92ms
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split(' '))

maze = []
l1 = []
for i in range(M+2):
    l1.append('0')
maze.append(l1)
for _ in range(N):
    l = list(sys.stdin.readline().strip())
    l.insert(0, '0')
    l.append('0')
    maze.append(l)
maze.append(l1)

distance = [[-1] * (M+2) for _ in range(N+2)]

graph = {}
for i in range(1,N+1): # 4
    for j in range(1, M+1): # 6
        graph[f'{i} {j}'] = [f'{i-1} {j}',f'{i} {j-1}',f'{i+1} {j}',f'{i} {j+1}']
# print(maze)
def maze_run(maze,distance,start, N, M):
    que = deque()
    a, b = map(int, start.split(' '))

    distance[a][b] = 1  # 시작점부터 1칸 시작
    que.append((a,b))
    while que:
        x,y  = que.popleft()

        # 자기자신
        for rr in graph[f'{x} {y}']: # 하위 타고 들어가기기
            ny, nx = map(int, rr.split(' '))
            # 자식
            if (distance[ny][nx] == -1) and (maze[ny][nx] == '1'):
                distance[ny][nx] = distance[x][y] + 1
                que.append((ny,nx))
    return distance[N][M]

print(maze_run(maze,distance,'1 1', N, M))
