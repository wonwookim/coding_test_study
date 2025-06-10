# 33432KB	52ms
import sys

T = int(sys.stdin.readline().strip()) # 테스트 케이스

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split()) # M가로 N새로 K 배추의 수
    ground = [[0] * M for _ in range(N)] 
    visited = [[False] * M for _ in range(N)] 
    baechu = []
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().strip().split()) # 배추의 위치
        ground[Y][X] = 1
        baechu.append((X,Y))
    direc = [(1,0),(0,1),(-1,0),(0,-1)]
    count = 0
    while baechu:
        b = baechu.pop()
        small_baechu = []
        if (visited[b[1]][b[0]] == False) and (ground[b[1]][b[0]]==1):
            visited[b[1]][b[0]] = True
            for d in direc: # 주변 땅 추가 
                x = d[0] + b[0]
                y = d[1] + b[1]
                if x >=0 and y>=0 and x <= M-1 and y <= N-1:
                    small_baechu.append((x,y))
            while small_baechu:
                b = small_baechu.pop()
                if (visited[b[1]][b[0]] == False) and (ground[b[1]][b[0]]==1):
                    visited[b[1]][b[0]] = True
                    for d in direc: # 주변 땅 추가 
                        x = d[0] + b[0]
                        y = d[1] + b[1]
                        if x >=0 and y>=0 and x <= M-1 and y <= N-1:
                            small_baechu.append((x,y))
            count +=1
    print(count)

