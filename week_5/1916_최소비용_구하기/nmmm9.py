import sys
import heapq

input = sys.stdin.readline

# 입력
n = int(input())  # 도시 개수
m = int(input())  # 버스 개수

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u -> v 가는 비용 w

start, end = map(int, input().split())

# 최소비용 테이블
INF = int(1e9)
distance = [INF] * (n+1)

# 다익스트라 함수
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))  # (비용, 도시)
    distance[start] = 0

    while queue:
        cost, now = heapq.heappop(queue)

        if distance[now] < cost:
            continue

        for next_city, next_cost in graph[now]:
            total_cost = cost + next_cost
            if total_cost < distance[next_city]:
                distance[next_city] = total_cost
                heapq.heappush(queue, (total_cost, next_city))

# 실행
dijkstra(start)

# 출력
print(distance[end])
