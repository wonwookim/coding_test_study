# 시간: 44ms, 메모리: 32600KB
# N : 세로 길이, M : 가로 길이
# 접근
    # graph, visited, count 만들기
        # visited: 방문 여부 (-1: dfs 내에서 방문 했을 경우, 무한 루프, 0: 방문 x, 1: 방문 O)
        # count: 방문했을 때, 해당 위치에서의 최대 횟수
    # 0,0에서 dfs 돌리기
        # dfs 중복 여부 확인
        # dfs가 아닌 이 전에 방문 여부 확인
        # 이전과 동일하게 상하좌우 파악
        # count와 비교하기 전에 target 값이 -1 즉 dfs내에서 방문했는지 -> 무한 루프 여부 확인
        # 무한루프일 경우 return -1 
        # 아닐 경우 그대로 진행

import sys
sys.setrecursionlimit(10**6) # 이거 안 하면 런타임 에러 발생해요

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
counts = [[0] * M for _ in range(N)]
# 상하좌우
ny = [0, 1, -1, 0]
nx = [1, 0, 0, -1]

def dfs(y, x):

    if visited[y][x] == -1: # dfs에서 또 다시 방문 한 경우
        return -1
    
    if counts[y][x] != 0:   # dfs가 아닌 이 전에 이미 방문했을 경우
        return counts[y][x]
    
    current = int(graph[y][x]) 
    count = 1
    visited[y][x] = -1 # dfs 내에서 방문 했을 때, -1로 두기    

    for idx in range(4):
        dy = y + (ny[idx] * current)
        dx = x + (nx[idx] * current)

        if 0 <= dy < N and 0 <= dx < M and graph[dy][dx] != 'H': # dy, dx는 N,M보다 클 수 없고, 그때 값은 H가 아닐 때,
            target = dfs(dy, dx)

            if target == -1: # dfs를 통해 얻은 값이 -1 -> 무한 루프
                return -1 # 빠져 나오기
            
            counts[dy][dx] = target
            count = max(count, target + 1)

    visited[y][x] = 1
    counts[y][x] = count
    return count

print(dfs(0,0))
