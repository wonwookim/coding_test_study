import sys
sys.setrecursionlimit(10**4)



N = int(input())
queen = [0] * N      # 딕셔너리 대신 리스트로 변경
count = 0

col_check = [False] * N
diag1_check = [False] * (2 * N - 1)
diag2_check = [False] * (2 * N - 1)

def dfs(row):
    global count
    for col in range(N):
        if col_check[col] or diag1_check[row+col] or diag2_check[row-col+N-1]:
            continue
        queen[row] = col                      # 퀸 배치 시도
        col_check[col] = True
        diag1_check[row+col] = True
        diag2_check[row-col+N-1] = True
                                   
        if row == N - 1:                  
            count += 1                    # 마지막 행 성공
        else:
            dfs(row + 1)                  # 다음 행으로 이동
        
        col_check[col] = False              # 초기화
        diag1_check[row+col] = False
        diag2_check[row-col+N-1] = False
dfs(0)
print(count)


