# 시간: 44ms, 메모리: 32776KB

# T: testcase
# M(가로), N(세로), K(배추 심어져있는 개수)
# X, Y (배추의 좌표)

# 접근
    # 그래프 그리기
    # 배추가 심어져있는(1) 곳에 대해 dfs 돌리기
    # visited를 사용하여 재방문 x
    # dfs가 끝날 때 마다 count를 하여 지렁이 개수를 파악
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# TestCase
for _ in range(T):
    M, N, K = map(int,input().split())
    graph = [[0] * (M) for _ in range(N)] # 전체 좌표
    visited = [[0] * (M) for _ in range(N)] # 방문 여부
    count = 0
    
    # dfs 함수
    def dfs(y, x):
        if visited[y][x] or graph[y][x] == 0 : # 방문했으면 빠져나오기
            return
        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i] 
            nx = x + dx[i]
            
            if 0 <= ny <= (N-1) and 0 <= nx <= (M-1) and not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(ny, nx)
    # 양배추 위치 graph에 반영    
    for _ in range(K): 
        baechu_x, baechu_y = map(int,input().split())
        graph[baechu_y][baechu_x] = 1
    
    for j in range(N): # 열에 대한 순환
        for i in range(M): # 행에 대한 순환
            if not visited[j][i] and graph[j][i] == 1: # 방문하지 않았을 경우
                dfs(j, i)
                count += 1
    print(count)
                
