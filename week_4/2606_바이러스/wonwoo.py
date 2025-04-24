# 시간 : 52ms, 메모리 : 34944KB
import sys
from collections import deque
input = sys.stdin.readline # 가독성을 위해 readlines 사용 x

N = int(input()) # 전체 컴퓨터 수
nodes = int(input()) # 연결 선 수


graph = {} # dict 형식으로 그리기, 양방향으로 그릴 예정 
visited = set() # 방문 여부는 set으로 1~N까지 넣어질 예정

# graph 그리기 : 양방향
for _ in range(nodes):
    start, end = map(int, input().strip().split()) # 들어오는 연결을 처리
    if graph.get(start) != None:  # start라는 key값이 존재하는 경우 -> end를 추가
        graph[start].append(end)
    else: # start라는 key가 존재하지 않는 경우 -> end를 담은 리스트 생성
        graph[start] = [end]
    
    if graph.get(end) != None:
        graph[end].append(start)
    else:
        graph[end] = [start]

def bfs(graph, start, visited): # bfs 함수수
    dq = deque([start]) # queue 생성
    visited.add(start) # 방문 업데이트
    count = 0 # 몇개 감염 됐는지 확인
    while dq : # queue가 존재하는 경우 계속 돌기
        i = dq.popleft() # queue 맨 앞의 값을 가져오기
        if i not in graph.keys(): # 그 값이 graph의 key에 존재하지 않는 경우 -> 예외 처리
            return 0
        for nx in graph[i]: # key 값이 존재하면 그 때, 연결된 컴퓨터들에 대해 돌기
            if nx not in visited: # 중복 방지
                visited.add(nx)
                dq.append(nx)
                count += 1
    return count

print(bfs(graph, 1, visited))