# import sys
# from collections import deque
# N = int(sys.stdin.readline().strip())
# color = []
# for _ in range(N):
#     color.append(sys.stdin.readline().strip())
# visited = [ [False]*len(color[0]) for _ in range(N)]
# visited2 = [ [False]*len(color[0]) for _ in range(N)]
# graph = {}
# for j in range(N):
#     for i in range(len(color[0])):
#         graph[f"{j} {i}"] = [(j-1, i), (j, i-1), (j+1, i), (j, i+1)]

# def rgb(visited,graph):
#     result = 0
#     que = deque()
#     for j in range(N):
#         for i in range(len(color[0])):
#             if visited[j][i] == False:
#                 col = color[j][i] # R
#                 que.append((j,i))
#                 while que:
#                     pop1 = que.popleft()
#                     a = int(pop1[0])
#                     b = int(pop1[1])

#                     visited[a][b] = True

#                     for xy in graph[f"{a} {b}"]:
#                         y = int(xy[0])
#                         x = int(xy[1])
#                         if (0 <= x < len(color[0])) and (0 <= y < N): # 범위 넘어가지 않도록
#                             if visited[y][x] == False: # 방문 안했고
#                                 if color[y][x] == col: # 색 같으면 추가
#                                     que.append(xy) # "0 1"
#                 result += 1
                                
#     return result

# print(rgb(visited,graph), end=' ')


# def rgb2(visited,graph):
#     result = 0
#     que = deque()
#     for j in range(N):
#         for i in range(len(color[0])):
#             if visited[j][i] == False:
#                 col = color[j][i] # R
#                 que.append((j,i))
#                 while que:
#                     pop1 = que.popleft()
#                     a = int(pop1[0])
#                     b = int(pop1[1])

#                     visited[a][b] = True

#                     for xy in graph[f"{a} {b}"]:
#                         y = int(xy[0])
#                         x = int(xy[1])
#                         if (0 <= x < len(color[0])) and (0 <= y < N): # 범위 넘어가지 않도록
#                             if visited[y][x] == False: # 방문 안했고
#                                 if (col == 'R') or (col == 'G'):
#                                     if (color[y][x] == 'R') or (color[y][x] == 'G'):# 색 같으면 추가
#                                         que.append(xy) # "0 1"
#                                 elif col == 'B':
#                                     if color[y][x] == 'B':
#                                         que.append(xy)
#                 result += 1
                                
#     return result

# print(rgb2(visited2,graph))
# 35016KB	72ms
import sys
from collections import deque

# 빠른 입력을 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# N: 그림의 크기 (NxN)
N = int(input())
# color: 그림을 2차원 리스트로 저장
color = [list(input().strip()) for _ in range(N)]

# 정상인의 방문 여부를 저장하는 2차원 리스트
visited_normal = [[False] * N for _ in range(N)]
# 색약인의 방문 여부를 저장하는 2차원 리스트
visited_weak = [[False] * N for _ in range(N)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
# x, y: 시작 좌표
# visited: 방문 여부 리스트
# is_weak: 색약 모드 여부 (True면 적록색약)
def bfs(x, y, visited, is_weak):
    queue = deque()
    queue.append((x, y))    # 시작점 큐에 삽입
    visited[x][y] = True    # 시작점 방문 처리
    current_color = color[x][y]  # 시작점 색 저장

    while queue:
        x, y = queue.popleft()  # 현재 좌표 꺼내기

        # 4방향 탐색
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 새로운 좌표가 범위 안에 있고 아직 방문 안했을 때
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                next_color = color[nx][ny]  # 이동할 좌표의 색

                # 적록색약인 경우
                if is_weak:
                    # R과 G를 같은 색으로 취급
                    if (current_color in 'RG' and next_color in 'RG') or (current_color == 'B' and next_color == 'B'):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                # 정상인 경우
                else:
                    if current_color == next_color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

# 정상인 영역 개수 세기
count_normal = 0
for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:  # 아직 방문하지 않은 곳이면
            bfs(i, j, visited_normal, False)  # BFS 돌리기 (정상 모드)
            count_normal += 1  # 하나의 영역 완료

# 색약인 영역 개수 세기
count_weak = 0
for i in range(N):
    for j in range(N):
        if not visited_weak[i][j]:  # 아직 방문하지 않은 곳이면
            bfs(i, j, visited_weak, True)  # BFS 돌리기 (색약 모드)
            count_weak += 1  # 하나의 영역 완료

# 결과 출력
print(count_normal, count_weak)