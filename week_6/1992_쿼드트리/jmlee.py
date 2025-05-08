#시간 36ms 메모리 33432KB
#IndexError 해결하는데에 애먹음. 왜 다른 문제들과 다르게 얘만 인덱스 에러가 날까?
import sys

input = sys.stdin.readline

N = int(input())
# matrix = [list(map(int, list(input().split()))) for _ in range(N)]
# 바보같은 실수.. 앞에 문제들은 공백이 있었지만, 얘는 공백이 없다!! 문제 예시를 잘 보자
matrix = [ [int(c) for c in input().strip()] for _ in range(N) ]
# strip()으로 문자만 가져오고 for문으로 글자 하나씩 가져오는 것
result = []

def quadtree(row, col, size):
    # 범위 벗어나지 않도록 체크
    if row + size > N or col + size > N:
        return
    val = matrix[row][col]
    # 1. 현재 영역이 모두 같은지 확인
    flag = True
    for i in range(row, row + size):
        for j in range(col, col + size):
            if matrix[i][j] != val:
                # 서로 다름
                flag = False
                break
        if not flag:
            break
    # 2. 같으면 카운트
    if flag:
        result.append(str(val))
    else:
        result.append('(')
        new_size = size // 2
        # size가 1 이상일 때만 분할
        if new_size > 0:
            for dy in range(2):
                for dx in range(2):
                    new_row = row + dy * new_size
                    new_col = col + dx * new_size
                    quadtree(new_row, new_col, new_size)
        result.append(')')
    return result

quadtree(0, 0, N)
print(''.join(result))
