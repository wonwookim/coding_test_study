# 시간: 384ms, 메모리: 42144KB
# F: 총 층, S: 현재 층, G: 도착해야하는 층, U: 위로 몇 칸, D: 아래로 몇 칸
# 접근
    # visited 생성 -> 방문 여부
    # bfs 이용 -> 
        # dq에 현재 층, 횟수 추가
        # 현재 층에서 위, 아래 각각 확인해서 조건에 맞으면 dq에 추가


# 원래 visited에 방문 여부가 아니라 기존 값에서 +1 하는 형식으로 진행
# 그랬을 때, 불필요한 덧셈 +=, 불필요한 조건문 추가    -> 584ms, 74068KB
import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int,input().strip().split())

visited = [0] * (F + 1)# 각 층별 방문 여부

def bfs(start, visited, G, U, D):
    if visited[start] != 0: # 방문 경험이 있으면 반복되는 층이 있기 때문에 도달 x
        return 'use the stairs'
    dq = deque([(start, 0)]) # 큐에 현재 층과 몇번 눌렀는지 추가
    while dq:
        x, count = dq.popleft()
        if x == G: # 도달했으면 count 보여주기
            return count
        up = x + U # 위로 올라간 층
        down = x - D # 아래로 내려간 층 
        if 1 <= up < len(visited) and visited[up] == 0:  # 1층부터 맨 윗 층 사이의 값이여야하고, 방문 이력이 없을 경우
            dq.append((up, count + 1)) # dq에 해당 층과, 한번 더 누른 값을 넣기
            visited[up] = 1 # 해당 층도 방문 했다고 하기

        if 1 <= down < len(visited) and visited[down] == 0: 
            dq.append((down, count + 1))
            visited[down] = 1
    return 'use the stairs'       

print(bfs(S, visited, G, U, D))




# def bfs(start, visited, G, U, D):
#     if visited[start] != 0: # 방문 경험이 있으면 반복되는 층이 있기 때문에 도달 x
#         return 'use the stairs'
#     dq = deque([start]) # 큐에 현재 층 집어넣기
#     while dq:
#         x = dq.popleft()
#         if x == G:
#             return visited[x]
#         up = x + U # 위로 올라간 층
#         down = x - D # 아래로 내려간 층
#         if 1 <= up < len(visited) and visited[up] == 0 and up != start:  -> up != start 로 불필요한 조건문
#             dq.append(up)
#             visited[up] += visited[x] +1 -> += 과 같은 필요하지 않은 연산
#         if 1 <= down < len(visited) and visited[down] == 0 and down != start:
#             dq.append(down)
#             visited[down] += visited[x] + 1
#     return 'use the stairs'