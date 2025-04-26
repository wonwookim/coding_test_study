# 시간: 64ms, 메모리: 34968KB
# N : 세로, M: 가로
# 접근
    # 2차원 배열의 graph -> dict는 인덱스 형식으로 접근하기 어려워서 list 사용
    # bfs 사용
        # 현재 좌표에서 상 하 좌 우 값을 비교하여 1 일 경우 그 값이 1일 경우 visited에 +1 하고, dq에 넣기기
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [] # 2차원 배열
for _ in range(N):
    line = list(input().strip())
    graph.append(line)

# visited = [[0] * M] * N  -> 이렇게 복사하니까 값이 다 바껴요 ㅠㅠㅠ
visited = [[0] * M for _ in range(N)] # 2차원 배열로 방문 여부 파악

def bfs(graph, y, x, visited):
    dq = deque([(y,x)]) # 들어온 값을 queue에 넣기
    ny = [0, 1, -1, 0]
    nx = [1, 0, 0, -1]
    visited[y][x] = 1 # 1로 바꾸기
    while dq :        
        y, x = dq.popleft()
        if x == M - 1  and y == N -1 : # 마지막까지 갔을 경우 
            return visited[y][x] # 마지막 위치의 값 -> 최소 칸 수
        for i in range(4):
            new_y = y + ny[i]
            new_x = x + nx[i]
            if 0 <= new_y < N and 0 <= new_x < M: # 범위에서 벗어나지 않도록
                if visited[new_y][new_x] == 0 and graph[new_y][new_x] == '1': # 한번도 방문 안 하고, 1에 해당 되는 애들만 다니기
                    visited[new_y][new_x] = visited[y][x] + 1 # 방금 온 값에서 + 1
                    dq.append((new_y, new_x))
    return -1
print(bfs(graph, 0,0, visited))