#시간 72ms 메모리 34944KB
import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int,input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

#시작지점 (0,0) 삽입
queue = deque([(0,0)])

#미로문제의 이동방향 설정: 우,좌,하,상
dx = [0,0,1,-1] 
dy = [1,-1,0,0]

#최단경로이므로 BFS
while queue:
    x,y = queue.popleft() #현재 위치 (x,y)
    for i in range(4): #현재 위치에서 4방향으로 이동가능한지 확인
        next_x, next_y = x+dx[i], y+dy[i] #이동할 다음위치 계산
        #이동할 좌표가 미로 범위(N,M) 내에 있는지 확인
        if 0 <= next_x < N and 0 <= next_y < M:
            if graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                #굳이 count변수 쓰지 않고 출력값에 +1로 저장
                graph[next_x][next_y] = graph[x][y] + 1 

#탐색종료 후 도착지(N-1,M-1)에 저장된 최소 이동칸수 저장
print(graph[N-1][M-1])