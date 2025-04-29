from collections import deque

# 입력
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 이동 방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어났다면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽이면 무시
            if maze[nx][ny] == 0:
                continue

            # 처음 방문하는 곳이면, 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    # 마지막 지점의 값이 최단거리
    return maze[n-1][m-1]

# 실행
print(bfs(0, 0))
