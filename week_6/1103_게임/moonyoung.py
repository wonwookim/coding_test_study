# 메모리 : 33528 KB, 36 ms
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 안 늘리면 런타임 에러,,

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board_input = sys.stdin.readline().strip()
    board.append(list(board_input))

# 위, 아래, 왼쪽, 오른쪽
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# (y,x)에서 최대 이동 횟수 저장
dp = []
for _ in range(N):
    dp.append([0] * M)

visited = []
for _ in range(N):
    visited.append([False] * M)

def dfs(x, y):
    # 보드 밖으로 나가면 0을 반환
    if x < 0 or x >= M or y < 0 or y >= N:
        return 0
    # 구멍인 경우도 종료 조건이므로 0 반환
    if board[y][x] == 'H':
        return 0
    
    if visited[y][x]:
        print(-1)
        sys.exit()

    # 이미 dp에 값이 저장되어 있다면 그 값을 사용
    if dp[y][x] != 0:
        return dp[y][x]

    visited[y][x] = True  
    max_move = 0  

    # 현재 칸의 숫자만큼 상하좌우 이동
    step = int(board[y][x])
    for dx, dy in directions:
        nx = x + dx * step
        ny = y + dy * step
        move_count = dfs(nx, ny) + 1
        if move_count > max_move:
            max_move = move_count

    visited[y][x] = False  
    dp[y][x] = max_move  
    return dp[y][x]

print(dfs(0, 0))