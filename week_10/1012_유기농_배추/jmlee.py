#시간 64ms, 메모리 34968KB
import sys
from collections import deque
input = sys.stdin.readline

# 접근법(로직)
# 1. 해당 가로*세로 크기에 맞는 빈 공간(0으로 채우기) 만들기
# 2. matrix에 있는 좌표값은 1로 변환
# 3. 연결된 덩어리는 한 번 방문하면 방문처리. 처음 방문하는 덩어리면 count += 1
# 4. 총 count 출력

def bfs(row,col):
    queue = deque([(row,col)])
    dx = [0,0,1,-1] # 좌우 이동 (열)
    dy = [1,-1,0,0] # 상하 이동 (행)
    visited[row][col] = True
    while queue:
        r,c = queue.popleft() 
        for i in range(4): 
            next_r = r+dy[i]
            next_c = c+dx[i] 
            if 0 <= next_r < N and 0 <= next_c < M:
                if farm[next_r][next_c] == 1 \
                and not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c))

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int,input().split()) # 가로, 세로, 배추 개수
    matrix = [ list(map(int,input().split())) for _ in range(K)]

    farm = [[0]*M for _ in range(N)]
    for x,y in matrix:
        farm[y][x] = 1 # y가 행(row), x가 열(col)
    count = 0

    visited = [[False]*M for _ in range(N)]
    # farm, visited 모두 [행][열] [row][col] 구조
    # 좌표 받을 때도 (row,col) 즉, (y,x 순서)
    for row in range(N):
        for col in range(M):
            if farm[row][col] == 1 and not visited[row][col]:
                bfs(row,col)
                count += 1
    print(count)
