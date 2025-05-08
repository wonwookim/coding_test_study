import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가 (기본 1000으로는 부족함) 자꾸 런타임에러나서 소라고동한테 물어봄 
input = sys.stdin.readline

n = int(input())

# 숲 입력: 각 칸의 대나무 양 
forest = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DP 배열: dp[x][y]는 (x,y)에서 출발했을 때 이동할 수 있는 최대 칸 수
dp = [[0] * n for _ in range(n)]

# DFS + Memoization
def dfs(x, y):
    # 이미 계산된 위치면 그대로 반환
    if dp[x][y] != 0:
        return dp[x][y]

    # 자기 자신 포함 최소 1칸 이동 가능
    dp[x][y] = 1

    # 상하좌우 인접한 칸 중, 더 많은 대나무가 있는 칸으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 체크
        if 0 <= nx < n and 0 <= ny < n:
            # 더 많은 대나무가 있는 칸으로만 이동 가능
            if forest[nx][ny] > forest[x][y]:
                # 이동한 칸까지 포함해서 최대 거리 갱신
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]

# 전체 좌표에 대해 가장 긴 경로 찾기
result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))  # (i,j)에서 시작한 경우 중 최댓값 갱신

print(result)  # 가장 길게 이동할 수 있는 칸 수
