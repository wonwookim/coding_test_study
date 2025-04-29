#시간 72ms 메모리 35004KB
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
a = [list(input()) for _ in range(N)]
queue = deque()

def bfs(x,y):
    queue.append((x,y)) #시작 위치에 큐 추가
    dx = [-1,0,1,0] # 상, 우, 하, 좌
    dy = [0,1,0,-1]
    visited[x][y] = 1 # 방문 표시
    while queue:
        x, y = queue.popleft()
        for d in range(4): #4방향 탐색
            nx = x + dx[d]
            ny = y + dy[d]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<N and 0<=ny<N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  
                queue.append((nx,ny)) # 다음 위치 큐에 추가

# 적록색약 아닌 경우
visited = [[0] * N for _ in range(N)]
count1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            bfs(i,j)
            count1 += 1

# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'

# 다시 방문 배열 초기화
visited = [[0] * N for _ in range(N)]
count2 = 0 #적록색약 시각에서의 구역 수
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            count2 += 1

print(count1, count2)