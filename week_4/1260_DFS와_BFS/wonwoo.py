# 시간 64ms, 메모리 35256KB

# 첫번째 줄 -> 정점의 개수, 간선의 개수, 탐색 시작 정점 번호
# 조건:
    # 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
    # 더이상 방문 할 수 있는 점이 없는 경우 종료
    # 정점 번호는 1번부터 N번까지
    # 입력으로 주어지는 간선은 양방향

# 접근:
    # 양방향 graph 생성 -> 오름차순 정렬
    # dfs
    # bfs

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int,input().split())

graph = {}

bfs_visited = set()
dfs_visited = set()

dfs_result = []
bfs_result = []

# 그래프 그리기
for _ in range(M):
    start, end = map(int, input().split())
    if graph.get(start, -1) == -1: # start라는 key가 없을 경우
        graph[start] = [end]
    else:
        graph[start].append(end)

    if graph.get(end, -1) == -1: # start라는 key가 없을 경우
        graph[end] = [start]
    else:
        graph[end].append(start)
graph = {key : sorted(value) for key, value in graph.items()} # 정렬 진행


# dfs
def dfs(graph, visited, node):
    global dfs_result # 함수 매개변수로 받는 변수들이 많아서 global로 뺴서 사용했습니다.. ㅎㅎ
    if node not in graph.keys(): #  예외 처리 -> node가 graph에서 연결 된 자식 노드가 없을 경우 빠져나오기
        dfs_result.append(str(node))
        return None
    visited.add(node) # 방문 여부 -> 변수에 값이 있는 경우, 이미 이 전에 방문했다는 것 -> 마지막엔 총 N개가 들어 옴
    dfs_result.append(str(node)) # 순서 넣기
    if len(graph.keys()) == len(visited): # 종료 조건 (방문 한 노드 개수와, graph의 key 값의 개수가 같으면 종료)
        return None
    for child_node in graph[node]: # 반복
        if child_node not in visited: # 중복 방지
            dfs(graph, visited, child_node) # 재귀함수를 통해 dfs 구현현
    return None

# bfs
def bfs(graph, visited, node):
    global bfs_result
    if node not in graph.keys(): # 동일한 예외 처리
        bfs_result.append(str(node))
        return None
    visited.add(node)
    dq = deque([node]) # queue를 이용하여 관리
    bfs_result.append(str(node)) # bfs 순서대로 넣기
    if len(graph.keys()) == len(visited): 
        return None
    while dq: # dq가 비어있을 때까지 순환
        parent_node = dq.popleft() # 맨 처음 들어온 애부터 처리
        for child_node in graph[parent_node]: # 순환
            if child_node not in visited: # 중복 방지
                dq.append(child_node) # queue에 child_node 넣기
                visited.add(child_node) # 방문 여부 추가
                bfs_result.append(str(child_node))
    return None

dfs(graph, dfs_visited, V)
bfs(graph, bfs_visited, V)
print(' '.join(dfs_result))
print(' '.join(bfs_result))
    