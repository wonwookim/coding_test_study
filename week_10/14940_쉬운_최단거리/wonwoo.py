# 시간: 408ms, 메모리: 44448KB

# n : 세로의 크기, m: 가로의 크기 (2 ≤ n & m ≤ 1000)
# 접근:
    # dfs
    # 2인 지역을 찾아서 bfs 돌기
    # dfs 깊이 들어갈 때마다 +1하기
    # 함수에 count를 받기

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split()) 
array = []
start_x = -1
start_y = -1
graph = [[-1] * m for _ in range(n)]


# 시작 지점 추출
for y in range(n):
    line = list(map(int,input().split()))
    if start_x == -1 and start_y == -1: # 아직 못 찾은 경우
        if 2 in line:
            start_y = y
            start_x = line.index(2)
    array.append(line)


# bfs를 이용한 시작 기준점으로부터 거리 구하기
def bfs(start_y, start_x, current_count):
    if graph[start_y][start_x] != -1 and array[start_y][start_x] != 0:
        return
    
    graph[start_y][start_x] = current_count
    array[start_y][start_x] = 1
    dq = deque([(start_y,start_x)])
    
    while dq:
        y, x = dq.popleft()
    
        nx = [0, -1, 0, 1]
        ny = [1, 0, -1, 0]
        
        for i in range(4):
            dy = y + ny[i]
            dx = x + nx[i]
            if 0 <= dy < n and 0 <= dx < m:
                if graph[dy][dx] == -1 and array[dy][dx] != 0: # 가려는 위치의 값이 0 (방문 x) 그리고 가려는 위치는 못 가는 곳이 아님
                    dq.append((dy, dx))
                    graph[dy][dx] = graph[y][x] + 1
                    array[dy][dx] = 1

bfs(start_y, start_x, 0)

# 값이 0이였던 애들을 -1에서 0으로 바꾸기
out = []
for i in range(n):
    row = []
    for j in range(m):
        if array[i][j] == 0:
            row.append('0')
        else:
            row.append(str(graph[i][j]))
    out.append(' '.join(row))

print('\n'.join(out))
    
