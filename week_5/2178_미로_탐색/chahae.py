# 34936	64
# 최단거리면  BFS!!!!!!
# 방향 벡터화 기억하기기

from collections import deque
import sys
input_ = sys.stdin.readline

N, M = map(int, input_().split())
maze = [list(map(int, input_().strip())) for _ in range(N)]
graph = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx= x + dx[i]
            ny= y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            if maze[nx][ny] == 1 :
                maze[nx][ny] = maze[x][y] + 1 
                queue.append((nx, ny))
    return maze[N-1][M-1]

print(bfs(0, 0))

            

               



        

# for i in range(N-1):
#     for j in range(M-1):
#         maze[i][j]
#         node = str(i)+str(j)
        
#         if (i > 0) and (j > 0):
#             if maze[i-1][j] == '1':
#                 graph[node].append(str(i)+str(j+1))
#             if maze[i][j-1] == '1':
#                 graph[node].append(str(i+1)+str(j))
#             if maze[i][j+1] == '1':
#                 graph[node].append(str(i)+str(j+1))
#             if maze[i+1][j] == '1':
#                 graph[node].append(str(i+1)+str(j))




# 노드 = 'i+j'
# 
