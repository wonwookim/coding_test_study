#시간 3928ms 메모리 71296KB
import sys

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
count_minus = 0
count_zero = 0
count_plus = 0

def paper_cut(row, col, size):
    global count_minus, count_zero, count_plus
    val = matrix[row][col]
    #1. 현재 영역이 모두 같은지 확인
    flag = True
    for i in range(row, row + size):
        for j in range(col, col + size):
            if matrix[i][j] != matrix[row][col]:
                # 서로 다름
                flag = False
                break
        if not flag:
            break

    #2. 같으면 카운트(같으면 num이 빈 집합)
    if flag:
        if val == -1:
            count_minus += 1
        elif val == 0:
            count_zero += 1
        else:
            count_plus += 1
    else:
        #3. 아니면 3등분 반복
        new_size = size // 3
        for dy in range(3):
            for dx in range(3):
                new_row = row + dy * new_size
                new_col = col + dx * new_size
                paper_cut(new_row, new_col, new_size)
    return count_minus,count_zero,count_plus

paper_cut(0,0,N)
print(count_minus)
print(count_zero)
print(count_plus)

