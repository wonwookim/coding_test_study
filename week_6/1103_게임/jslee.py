import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())
raw = [list(input().strip()) for _ in range(N)]

# 'H'는 0으로 처리하고 나머지는 int로 변환
board = []
for row in raw:
    new_row = []
    for cell in row:
        if cell == 'H':
            new_row.append(0)
        else:
            new_row.append(int(cell))
    board.append(new_row)

dp = [[-1]*M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False]*M for _ in range(N)] #무한루프 감지
cycle = [False] # 사이클 발동하면 켜짐

def dfs(x, y):
    if cycle[0]:  # 이미 사이클 감지되었으면 더 이상 계산할 필요 없음
        return 0
    if not (0 <= x < N and 0 <= y < M) or board[x][y] == 0:
        return 0
    if visited[x][y]:
        cycle[0] = True  # 사이클 감지
        return 0
    if dp[x][y] != -1:
        return dp[x][y]

    visited[x][y] = True
    dp[x][y] = 0
    step = board[x][y]

    for d in range(4):
        nx = x + dx[d] * step
        ny = y + dy[d] * step
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    visited[x][y] = False
    return dp[x][y]

result = dfs(0, 0)
if cycle[0]:
    print(-1) 
else:
    print(result)
