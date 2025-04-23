#시간 860ms 메모리 33576KB
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
    for neighbor in sorted(graph.get(start, [])):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

import sys
case_num = int(sys.stdin.readline())  # 테스트 케이스의 개수
for _ in range(case_num):
    n = int(sys.stdin.readline())  # 순열의 크기
    edges = list(map(int, sys.stdin.readline().split()))
    nodes = list(range(1,n+1))

    graph = {node: set() for node in nodes}
    for j in range(n):
        a, b = nodes[j], edges[j]
        graph[a].add(b)
        graph[b].add(a)
    
    visited = set()
    count = 0
    for node in nodes:
        if node not in visited:
            dfs(graph, node, visited) #이 노드와 연결된 모든 노드를 visited에 추가
            #하나의 연결요소 전체가 방문된다
            count += 1
    print(count)

##################################

#시간 144ms 메모리 32412KB
def find_cycles(edges,n):
    visited = [False] * (n+1) #1부터 시작하므로
    count = 0

    for i in range(1, n+1):
        if not visited[i]:
            num = i
            while not visited[num]:
                visited[num] = True
                num = edges[num] #순열에서 다음 숫자로 이동, edges는 순열 리스트
            count += 1
    return count
            
import sys
case_num = int(sys.stdin.readline())  # 테스트 케이스의 개수
for _ in range(case_num):
    n = int(sys.stdin.readline())  # 순열의 크기
    edges = [0]+ list(map(int, sys.stdin.readline().split()))
    print(find_cycles(edges, n))

