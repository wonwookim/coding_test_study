## 메모리 : 41956KB 시간 : 416ms

import sys
from collections import deque

input = sys.stdin.readline  

F, S, G, U, D = map(int, input().split())

# 1층부터 F층까지의 방문 여부를 저장할 리스트 (초기값 False)
visited = [False] * (F + 1)

def bfs():
    # 큐에는 (현재_층, 버튼_누른_횟수) 형태로 저장
    queue = deque([(S, 0)])
    visited[S] = True  # 시작 층 방문 처리

    while queue:
        floor, moves = queue.popleft()  # 큐에서 현재 상태 꺼내기
        if floor == G:                   # 목표 층에 도달했는지 확인
            return moves                # 누른 횟수 반환

        # 위(U)와 아래(D) 두 가지 버튼 이동을 시도
        for next_floor in (floor + U, floor - D):
            # 이동한 층이 1~F 범위 내이고, 아직 방문하지 않았다면
            if 1 <= next_floor <= F and not visited[next_floor]:
                visited[next_floor] = True               # 방문 처리
                queue.append((next_floor, moves + 1))    # 누른 횟수 1 증가시켜 큐에 추가

    return -1  # 목표 층에 도달하지 못하면 -1 반환

result = bfs()  # BFS 실행 결과 저장
if result == -1:
    print("use the stairs")  # 이동 불가능한 경우
else:
    print(result)            # 최소 버튼 누른 횟수 출력
