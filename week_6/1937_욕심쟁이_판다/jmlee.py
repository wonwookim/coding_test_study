#시간 756ms 메모리 52152KB

#DFS랑 DP(메모이제이션) 사용하기
#모든 칸에 대해 '최장 경로 길이'를 구해야한다
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘리기
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

#아직 계산 안한 값
dp = [[0]*N for _ in range(N)]

#상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(row,col):
    #이미 계산된 칸은 바로 반환
    if dp[row][col] != 0:
        return dp[row][col]
    
    #자기자신만 먹고 끝나는 경우
    dp[row][col] = 1

    #상하좌우 탐색
    for k in range(4):
        next_row = row + dy[k]
        next_col = col + dx[k]

        #인덱스값 초과하지 않게 & 다음 대나무가 많은 쪽으로 이동
        if 0 <= next_row < N and 0 <= next_col < N \
        and matrix[next_row][next_col] > matrix[row][col]:
            dp[row][col] = max(dp[row][col], 1 + dfs(next_row,next_col))
    return dp[row][col]

#모든 칸에 대해 dfs 호출하여 최댓값 갱신
answer = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] == 0:
            dfs(i,j)
        answer = max(answer, dp[i][j])

print(answer)

#########################

#재귀말고 반복문(스택)으로 풀기
