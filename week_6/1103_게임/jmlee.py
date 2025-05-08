#시간40ms  메모리 33528KB
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘리기
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]


#아직 계산 안한 값
dp = [[0]*M for _ in range(N)]
#방문 중인지 여부 계산
visited = [[False]*M for _ in range(N)]

#상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(row,col):
    if matrix[row][col] == 'H':
        return 0

    if visited[row][col]:
        print(-1)
        sys.exit()

    if dp[row][col] != 0:
        return dp[row][col]
    
    visited[row][col] = True
    dp[row][col] = 1
    
    #상하좌우 탐색
    for k in range(4):
        dist = int(matrix[row][col])

        next_row = row + dy[k]*dist
        next_col = col + dx[k]*dist

        if 0 <= next_row < N and 0 <= next_col < M \
        and matrix[next_row][next_col] != 0:
            dp[row][col] = max(dp[row][col], 1+ dfs(next_row,next_col))
    
    visited[row][col] = False
    return dp[row][col]


print(dfs(0,0))