# 시간: 72ms, 메모리: 350004KB

# N : 보드의 크기 (2 <= N <= 100)
# K : 사과의 개수 (0 <= K <= 100)
# 사과의 위치 (행, 열) -> (1, 1)은 존재 x
# L: 뱀의 방향 변환 횟수
# L개의 뱀의 방향 변환 정보 (게임 시작 시작 시간으로부터 X초, 방향(L, D))

# 조건
    # 뱀은 몸 길이를 늘려 머리를 다음칸에 위치
    # 만약 벽이나 자기자신의 몸과 부딪히면 게임 끝
    # 이동한 칸에 사과가 있다면, 그 칸에 있던 사과는 없어지고 꼬리 움직이지 않음
    # 이동한 칸에 사과가 없으면, 몸 길이를 줄여 꼬리가 위치한 칸을 비움

# 접근
    # 사과의 위치가 담긴 2차원 배열 생성
    # 이동 경로는 (행, 열) 방식으로 덱으로 표현
    
    # 방향 변환 방법
        # 길이가 4인 리스트 [0,0,0,0]으로 [상,하,좌,우]를 표현
        # 각 [상, 하, 좌, 우] 일 때 L,D 방향 전환을 나타내는 리스트 표현
            # [[(-1, 0),(1, 0)], [(1,0), (-1, 0)], [(0, 1),(0, -1)], [(0, -1),(0, 1)]]
            
    # 초 단위마다 몸을 불려나감 (덱에 저장)
    # 조건에 걸리지 않게 움직이기
    

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

# 전체 판을 나타내는 배열
x, y = 1, 1
# 사과 위치가 담긴 리스트 생성
apple_list = set()
for _ in range(K):
    apple_x, apple_y = map(int, input().split())
    apple_list.add((apple_x, apple_y))


C = int(input()) # 방향 전환 횟수
change_list = deque() # 방향 전환 내용을 담은 덱
for _ in range(C):
    time, direction = map(str, input().split())
    change_list.append((int(time), direction))
# 방향 변환 방법을 담은 리스트 (우, 하, 좌, 상) -> 이거를 잘 봐야함
dx = [0,   1,   0,  -1]   # x 좌표 변화 (가로 이동)
dy = [1,   0,  -1,   0]
direction = 0

# 뱀의 몸집
snake = deque()
snake.append((x, y))
# 게임 시간
time = 0
apple = 0

# 뱀 움직이기
while True:
    time += 1
    
    nx, ny = x + dx[direction], y + dy[direction]    
    if not (1 <= nx <= N and 1 <= ny <= N) or (nx, ny) in snake:
        break
    
    snake.append((nx,ny))
    
    # 사과 있는지 확인 -> 있을 경우 꼬리 생존
    if (nx,ny) in apple_list:
        apple_list.remove((nx, ny))     
    else:
        remove_x, remove_y = snake.popleft()
    
    # 방향 전환 여부 확인하기
    if change_list and change_list[0][0] == time:
        change_time, change_direct = change_list.popleft()
        if change_direct == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

    # 이동 방향과 이동해야하는 좌표를 찾기    
    x, y = nx, ny
    
print(time)
            
        
    
    