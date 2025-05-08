import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def solve(N, arr):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    dp = [[-1] * N for _ in range(N)]

    def dfs(x, y):
        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 1

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > arr[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

        return dp[x][y]

    max_len = 0 #판다가 움직이는 최대 길이
    for i in range(N):
        for j in range(N):
            max_len = max(max_len, dfs(i, j)) #최대 길이 갱신

    return max_len


# 실행
print(solve(N, arr))
