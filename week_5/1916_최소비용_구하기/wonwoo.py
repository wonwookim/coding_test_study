# 시간: 296ms, 메모리: 58232KB
# N : 도시 개수, M : 버스 개수
# 마지막 줄: 시작 도시, 도착 도시
# 접근
    # 그래프 생성 -> {1 : [(2,2), (3,3)]} 이런식으로 key는 도시 번호, value는 list((이동 도시, 비용))
    # dfs -> 재귀함수를 통해 시작 지점에서 갈 수 있는 모든 경우의수 다 구한 후, 그들의 총 비용의 min 값을 뱉어내기
    # 계속 루프 돌아서 x 
    # 다익스트라 알고리즘 사용
        # 최소 비용 문제에서 사용 -> heapq 사용 -> heapq는 내부적으로 정렬을 자동으로 해줌

import sys
import heapq
input = sys.stdin.readline

N = int(input()) # 도시 개수
M = int(input()) # 버스 개수
graph = {} # 그래프 그리기
for _ in range(M): # {1: [(2, 2), (3, 3), (4, 1), (5, 10)], 2: [(4, 2)], 3: [(4, 1), (5, 1)], 4: [(5, 3)]}
    start, end, cost = map(int, input().strip().split())
    if graph.get(start, -1) != -1:
        graph[start].append((end,cost))
    else:
        graph[start] = [(end, cost)]
at, to = map(int,input().strip().split()) #출발지, 도착지
costs = [1e9] * (N + 1) # 1 X 10 ^ 9 -> 비용을 엄청 크게 잡음
def dijkstra(start,costs):
    heap = []
    heapq.heappush(heap, (0, start)) # heapq 생성 (누적 비용, 도시) -> 누적 비용에 따라 오름차순 정렬
    costs[start] = 0 # 처음 시작 장소의 cost는 0으로 설정
    while heap:
        cost, station = heapq.heappop(heap) # cost, 도시 정보
        if graph.get(station, -1) == -1 or costs[station] < cost: # 예외 처리: station이 만약 graph의 key값에 없거나, 비용이 이전 비용보다 클 경우 지나가기기
            continue
        for next, pay in graph[station]: # 반복문
            if costs[next] > cost + pay: # heapq에 넣기 전에 해당 도시의 비용이 cost+pay보다 클 경우에만 진행 -> 낮추는 방향
                heapq.heappush(heap, (cost+pay, next))
                costs[next] = cost + pay
dijkstra(at, costs)
print(costs[to])
