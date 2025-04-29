# 메모리: 32984KB, 시간: 60ms


import sys
sys.setrecursionlimit(100000) # 재귀 제한 해제

input = sys.stdin.readline  
N = int(input().strip()) 
graph = [list(input().strip()) for _ in range(N)] 

# 방문 배열
visited_normal = [[False] * N for _ in range(N)] # 일반인용
visited_rg = [[False] * N for _ in range(N)] # 색맹용

# 방향 벡터 (상하좌우)
dx = [-1, 1, 0, 0] # X축 변화량
dy = [0, 0, -1, 1] # Y축 변화량

# DFS 함수 정의
def dfs(x, y, visited, color_group):
    visited[x][y] = True
    current_color = color_group[x][y]

    for i in range(4): #상하좌우에 이동 가능한 색 있는지 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if color_group[nx][ny] == current_color:
                dfs(nx, ny, visited, color_group)

# 일반
count_normal = 0
for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            dfs(i, j, visited_normal, graph)
            count_normal += 1

# 적록색약 → R을 G로 통일
count_rg = 0
graph_rg = [['G' if color == 'R' else color for color in row] for row in graph]

for i in range(N):
    for j in range(N):
        if not visited_rg[i][j]:
            dfs(i, j, visited_rg, graph_rg)
            count_rg += 1

print(count_normal, count_rg)
