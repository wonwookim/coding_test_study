#58232KB	312ms
import sys
import heapq
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = {}
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split(' '))
    if graph.get(a):
        graph[a].append((b,c))
    else:
        graph[a] = [(b,c)]

start, end = map(int, sys.stdin.readline().strip().split(' '))

INF = int(1e9)
distance = [INF] * (N+1)
heap = []
# start 부터 시작
distance[start] = 0
heapq.heappush(heap, (0, start)) # 거리 지점 -> 거리 기준 최소힙
while heap:
    dist, now = heapq.heappop(heap)
    # 이미 더 짧은 거리로 방문한 적이 있다면 skip
    if distance[now] < dist:
        continue

    if graph.get(now):
        for next_idx, next_idx_dist in graph[now]: # 그래프는 지점, 거리리
            new_dist = next_idx_dist + dist
            if distance[next_idx] > new_dist:
                distance[next_idx] = new_dist # 갱신신
                heapq.heappush(heap, (new_dist, next_idx)) # 거리 지점 -> 거리 기준 최소힙

print(distance[end])