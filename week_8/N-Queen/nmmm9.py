#한 행에 퀸을 하나씩 놓고, 다음 행으로 내려가며 재귀 탐색

#같은 열, 대각선에 퀸이 있는지 체크하면서 백트래킹

# 32412kb	31396ms

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
ans = 0

cols = [0] * n         
diag1 = [0] * (2 * n)    
diag2 = [0] * (2 * n)    

def dfs(row):
    global ans
    if row == n:
        # N개의 퀸을 모두 안전하게 놓은 경우
        ans += 1
        return

    for col in range(n):
        d1 = row + col               # 오른쪽아래 대각선 
        d2 = row - col + n - 1       # 왼쪽아래 대각선 (음수 방지)

        # 현재 위치에 퀸을 놓을 수 있는지 확인
        if cols[col] == 0 and diag1[d1] == 0 and diag2[d2] == 0:
            # 퀸 배치
            cols[col] = diag1[d1] = diag2[d2] = 1
            dfs(row + 1)  
            # 백트래킹
            cols[col] = diag1[d1] = diag2[d2] = 0

dfs(0)

print(ans)




