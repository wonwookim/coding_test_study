# 시간: 36ms, 메모리: 32412KB

# N : 재료의 개수
# 접근:
    # 백트레킹을 통해 모든 조합을 구하기
    # 그 조합에서 신맛과 쓴 맛의 차이가 가장 적은 조합을 구하기

import sys
input = sys.stdin.readline

N = int(input())

flavors = [list(map(int,input().split())) for _ in range(N)]
# visited = [False] * (N + 1)
result = 1e9

def backtracking(idx, sour, bitter):
    global result
    if idx != -1:
        result = min(result, abs(sour - bitter))
    if idx == N:
        return 
    for i in range(idx + 1, N):
        # if not visited[i]: # 방문하지 않았을 때,
            # visited[i] = True
            backtracking(i, sour * flavors[i][0], bitter + flavors[i][1])
            # visited[i] = False
    
backtracking(-1, 1, 0)
print(result)