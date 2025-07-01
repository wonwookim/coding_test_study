# 메모리: 100520KB 시간: 2360ms


from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())

# 토마토 상태를 저장할 2차원 리스트 (N행 M열)
# grid[y][x] = 1 (익은), 0 (안 익은), -1 (없음)
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# BFS에 사용할 큐 + 초기 익은 토마토 좌표 저장
queue = deque()
for y in range(N):
    for x in range(M):
        if grid[y][x] == 1:
            queue.append((y, x))  # (행, 열)

# 이동 방향 정의: 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS 시작
while queue:
    y, x = queue.popleft()
    
    # 현재 위치에서 4방향으로 탐색
    for direction in range(4):
        ny = y + dy[direction]
        nx = x + dx[direction]
        
        # 격자 범위 안에 있고, 익지 않은 토마토일 경우
        if 0 <= ny < N and 0 <= nx < M and grid[ny][nx] == 0:
            # 익게 만들고, 며칠째인지 기록 (현재 일수 + 1)
            grid[ny][nx] = grid[y][x] + 1
            queue.append((ny, nx))

# BFS 종료 후 결과 판단
max_day = 0
for row in grid:
    for value in row:
        if value == 0:
            # 익지 않은 토마토가 남아 있으면 실패
            print(-1)
            sys.exit(0)
        # 최댓값 갱신 (며칠째에 익었는지)
        max_day = max(max_day, value)

# 시작이 1이었으므로, 결과는 max_day - 1
print(max_day - 1)
