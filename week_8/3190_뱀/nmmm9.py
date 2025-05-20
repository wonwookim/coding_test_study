# 뱀의 몸은 deque로 관리 (머리 ↔ 꼬리)

# 현재 방향은 dx, dy 배열로 회전

# 매 초마다 위치 이동 → 사과 확인 → 몸 충돌 확인

# 34984kb	64ms

from collections import deque

N = int(input())  # 보드 크기
K = int(input())  # 사과 

board = [[0] * N for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1  

L = int(input())
turns = dict()
for _ in range(L):
    t, d = input().split()
    turns[int(t)] = d  # 시간별 방향 전환 저장

# 방향: 오른, 아래, 왼, 위   >> 시계방향 순환때문에 이렇게 저장
dx = [1, 0, -1, 0]   
dy = [0, 1, 0, -1]
dir = 0  # 처음엔 오른쪽

snake = deque()
snake.append((0, 0))  # 뱀 초기 위치
time = 0

x, y = 0, 0

while True:
    time += 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 벽에 부딪히면 끝
    if not (0 <= nx < N and 0 <= ny < N):
        break
    # 자기 몸에 부딪히면 끝
    if (ny, nx) in snake:
        break

    # 이동
    snake.append((ny, nx))

    if board[ny][nx] == 1:  # 사과 있으면 안 지움 (길이 늘어남)
        board[ny][nx] = 0
    else:  # 사과 없으면 꼬리 자름
        snake.popleft()

    x, y = nx, ny  # 머리 위치 갱신

    # 회전 시점
    if time in turns:
        if turns[time] == 'D':
            dir = (dir + 1) % 4  # 오른쪽 회전
        else:
            dir = (dir - 1) % 4  # 왼쪽 회전

print(time)


