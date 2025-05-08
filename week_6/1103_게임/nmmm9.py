#메모리: 33512kb 시간: 36ms

import sys
sys.setrecursionlimit(10**6) # << 소라고동
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[0] * m for _ in range(n)]  # x,y 에서 출발할 때 최대 이동 횟수
visited = [[False] * m for _ in range(n)]  

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or board[x][y] == 'H':
        return 0  # 구멍(H) 또는 범위 밖이면 종료

    if visited[x][y]:
        print(-1)  # 같은 길 반복 시 즉시 종료
        sys.exit(0)

    if dp[x][y] != 0:
        return dp[x][y]  # 이미 계산된 위치면 값 반환

    visited[x][y] = True  # 현재 위치 방문 처리
    move = int(board[x][y])  # 현재 칸의 숫자만큼 이동

    for i in range(4):
        nx = x + dx[i] * move
        ny = y + dy[i] * move
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    visited[x][y] = False  # 백트래킹 
    return dp[x][y]

print(dfs(0, 0))
