# 시간 336ms 메모리 61304KB
import sys
import heapq 

input = sys.stdin.readline

n = int(input()) 
m = int(input())
# 빈 그래프 만들기
graph = [[] for _ in range(n+1)]

for _ in range(m):
    # a번 도시에서 b번 도시로 가는 데 드는 비용이 cost
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
        
start, end = map(int, input().split())

# 초기 최소비용은 매우 큰 수로 설정(무한대 개념)
INF = int(1e9)
costs = [INF for _ in range(n+1)] #실제로 비용이 갱신될때만 값이 바뀜

heap = []
costs[start] = 0
heapq.heappush(heap, [0, start]) #(비용, 도시)

#다익스트라 알고리즘 
while heap:
    # 가장 비용이 적은 경로 꺼냄
    cur_cost, cur_v = heapq.heappop(heap)
    # 이미 더 좋은 경로가 있을 경우, 무시
    if costs[cur_v] < cur_cost:
        continue
    # 현재 도시와 연결된 모든 도시 탐색
    for next_v, next_cost in graph[cur_v]:
        # 현재 도시까지의 비용 + 다음 도시로 가는 비용
        sum_cost = cur_cost + next_cost
        # 이 경로가 더 짧으면 갱신 후 우선순위 큐에 입력
        if sum_cost >= costs[next_v]:
            continue
        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])
    
print(costs[end])