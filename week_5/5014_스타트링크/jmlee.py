#시간 556ms 메모리 74136KB
import sys
from collections import deque

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())  
#각 층 방문 여부 및 몇 번 이동했는지 기록
check = [0 for _ in range(F + 1)]  


def bfs():  
    queue = deque()  
    queue.append(S) #현재 층 큐에 삽입

    check[S] = 1  #현재 층 방문 처리

    while queue:  
        y = queue.popleft() #현재 층 꺼내기
        #목표 층에 도착했다면
        if y == G:  
            return check[y] - 1  #이동횟수 반환(처음에 출발층을 1로 기록했으니 -1)
        else:
            #y+U는 위로 이동, y-D는 아래로 이동
            for x in (y + U, y - D):
                #층이 건물 범위 안에 있고, 아직 방문하지 않았다면
                if (0 < x <= F) and check[x] == 0:  
                    check[x] = check[y] + 1  #이동횟수 기록
                    queue.append(x)  #다음탐색을 위해 큐에 삽입
    return "use the stairs"  

print(bfs())