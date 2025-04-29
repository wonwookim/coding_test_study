# 메모리: 58232KB, 시간: 296ms



import sys
import heapq


# 문제 입력 및 가중치 그래프 생성 (인접 리스트)
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost)) # 방향 있는 그래프이므로 하나만 생성

start, end = map(int, input().split())


# 다익스트라 알고리즘과 우선순위 큐
#비용 초기값 설정
INF = int(1e9)  # 충분히 큰 값, 무한 값
distance = [INF] * (N + 1)
distance[start] = 0

hq = []
heapq.heappush(hq, (0, start)) # 시작

while hq:  
    current_cost, current_node = heapq.heappop(hq) # 다음 목적지 계산

    if distance[current_node] < current_cost:  # 비용 더 크면 갱신 X
        continue

    # 인접 노드들을 하나씩 보고 더 짧은 경로 발견하면 업데이트
    for location, location_cost in graph[current_node]:
        if distance[location] > current_cost + location_cost:  # 최소비용 갱신
            distance[location] = current_cost + location_cost  # 반직관적
            heapq.heappush(hq, (distance[location], location))

print(distance[end])
