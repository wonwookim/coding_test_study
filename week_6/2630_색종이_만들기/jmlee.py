#시간 44ms  메모리 32412KB
import sys

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
count_blue = 0
count_white = 0

def paper_color(row, col, size):
    global count_blue, count_white
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
        if val == 1:
            count_blue += 1
        else:
            count_white += 1
    else:
        #3. 아니면 3등분 반복
        new_size = size // 2
        for dy in range(2):
            for dx in range(2):
                new_row = row + dy * new_size
                new_col = col + dx * new_size
                paper_color(new_row, new_col, new_size)
    return count_blue,count_white

paper_color(0,0,N)
print(count_white)
print(count_blue)

