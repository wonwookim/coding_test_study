#메모리: 33432kb 시간: 36ms

import sys
input = sys.stdin.readline

n = int(input())
video = [list(map(int, list(input().strip()))) for _ in range(n)]

result = []  # 리스트에 문자 누적

# 현재 영역이 모두 같은 숫자인지 확인
def is_same(x, y, size):
    base = video[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != base:
                return False
    return True

# 분할 정복 함수
def divide(x, y, size):
    if is_same(x, y, size):
        result.append(str(video[x][y]))  # 0 또는 1을 문자열로 추가
        return
    
    result.append('(')  # 분할 시작
    
    new_size = size // 2
    divide(x, y, new_size)                         # 왼쪽 위
    divide(x, y + new_size, new_size)              # 오른쪽 위
    divide(x + new_size, y, new_size)              # 왼쪽 아래
    divide(x + new_size, y + new_size, new_size)   # 오른쪽 아래
    
    result.append(')')  # 분할 종료

# 시작
divide(0, 0, n)

# 리스트를 문자열로 합쳐서 출력
print(''.join(result))
