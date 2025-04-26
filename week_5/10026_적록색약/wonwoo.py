# 시간: 68ms, 메모리: 35016KB
# N * N : 그림 총 크기
# 접근
    # graph 만들기
    # visited 만들기(방문 여부)
    # count 총 구역 개수
    # 구역 전체에 대해 bfs를 돌림 -> 위치마다 bfs
    # bfs -> 상하좌우마다 현재 색과 비교하여 같으면 dq에 추가, visited 갱신 -> return 1 해서 영역 1개 생성된걸 알려줌
# 처음 안 사실, global 변수는 수정하지 않고 읽기만 하는 경우 global을 함수에서 작성하지 않아도 됨
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
blindness_count = 0 # 전체 구역 개수
not_blindness_count = 0 # 전체 구역 개수
# 그래프 만들기
graph = [list(input().strip()) for _ in range(N)]
# visited 만들기
blindness_visited = [[False] * N for _ in range(N)]
not_blindness_visited = [[False] * N for _ in range(N)]

def bfs(visited, y, x, red_green_color_blindness = False): # 적록색약 여부를 나타내는 변수를 받음 -> 이거 받아서 더 가독성이 떨어지는 것 같음음
    dq = deque([(y,x)])
    nx = [0, 1, 0, -1]
    ny = [1, 0, -1, 0]
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            dy, dx = y + ny[i], x + nx[i]
            if 0 <= dx < N and 0 <=  dy < N and not visited[dy][dx]: # dy,dx가 0부터 N-1 사이의 값이면서, 방문하지 않았을 경우
                if red_green_color_blindness: # 적록 색약인 경우
                    # 기존 값이 B일 때, graph[dy][dx]와 같거나, 기존 값이 B가 아니고, graph[dy][dx]도 B가 아닌 경우우
                    if (graph[y][x] == 'B' and graph[dy][dx] == graph[y][x]) or (graph[y][x] != 'B' and graph[dy][dx] != 'B'): 
                        dq.append((dy, dx))
                        visited[dy][dx] = True
                else: # 적록 색약이 아닌 경우
                    if graph[dy][dx] == graph[y][x]: # 기존 값과. dydx의 값이 같은 경우우
                        dq.append((dy, dx))
                        visited[dy][dx] = True
    return 1

for j in range(N):
    for i in range(N):
        if not not_blindness_visited[j][i] : # 색약이 아닐떄 그 위치에 방문 안 했을 경우 진행
            not_blindness_visited[j][i] = True 
            not_blindness_count += bfs(not_blindness_visited, j, i) # 영역을 다 칠했을 때, 1을 받기 때문에 count에 추가

        if not blindness_visited[j][i] :
            blindness_visited[j][i] = True
            blindness_count += bfs(blindness_visited, j, i, True)
        
print(not_blindness_count, blindness_count)
