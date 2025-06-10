# 시간: 684ms, 메모리: 66174KB

# N: 정점의 개수, M: 간선의 개수 (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# u, v (간선의 양 끝 점)

# 접근:
    # 일단 그래프 그리기
    # 그래프를 for로 돌려서 visited 됐는지 안 됐는지 확인
    # 그리고 visited를 다 하고 dfs에서 빠져나왔을 때, count 1을 하기
    
import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N, M = map(int, input().split())

graph = {i+1 : [] for i in range(N)} # 1부터 N까지의 그래프 그리기
visited = [False] * (N + 1) # 각 점의 방문여부

def dfs(start):
    if visited[start]:
        return
    visited[start] = True # 방문했다고 바꾸기
    
    for neighbor in graph[start] :
        if not visited[neighbor]: # 방문하지 않았을 경우
            dfs(neighbor)
        
        
count = 0
for _ in range(M):
    u, v = map(int,input().split()) # 간선의 양 끝 점
    graph[u].append(v)
    graph[v].append(u)
    
for key in range(1, N + 1):
    if not visited[key] : # 방문 안 했을 경우
        dfs(key)
        count += 1
print(count)
        
        
        
        
    