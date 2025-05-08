# 메모리 : 58232 KB, 시간 : 280 ms
import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

for _ in range(M) :
  start, end, cost = map(int, sys.stdin.readline().split())
  graph[start].append((end, cost))

start, end = map(int, sys.stdin.readline().split())

INF = int(1e9)

def min_cost(start) :
  distance = [INF] * (N+1)
  distance[start] = 0

  queue = []
  heapq.heappush(queue, (0, start))

  while queue :
    dist, now = heapq.heappop(queue)

    if distance[now] < dist :
      continue
    
    for next_node, cost in graph[now] :
      total_cost = dist + cost
      if total_cost < distance[next_node] :
        distance[next_node] = total_cost
        heapq.heappush(queue, (total_cost, next_node))

  return distance

result = min_cost(start)
print(result[end])