# 시간: 44ms, 메모리: 32412KB
# 최대 시간 복잡도: 114,688 : (128 * 128) * log_2(128) -> for를 통한 is_same 확인 작업 * 재귀함수(2분할)
# N : 종이의 크기(N X N)
# 접근:
    # 재귀함수 사용
    # 전체가 같은 색이면 해당 색에 count + 1
    # 1개라도 다른 색이 존재하면 절반으로 가로 세로 나누기
    # 위의 방식 그대로 진행


import sys
input = sys.stdin.readline
N = int(input() ) # 종이의 크기

array = [list(map(int,input().strip().split())) for _ in range(N)]
answer = { i : 0 for i in range(0, 2)}

def area_count(x, y, n):
    key = array[y][x]
    is_same = True
    for row in range(y, y + n):
        for char in range(x, x + n):
            if array[row][char] != key:
                is_same = False
                break
        if not is_same:
            break

    if is_same : # 모든 요소가 같은 경우
        answer[key] += 1
        return 
    
    # 하나라도 다른 경우 분할하기
    batch_size = n//2
    for dy in [0, 1]:
        for dx in [0, 1]:
            ny = y + dy * batch_size
            nx = x + dx * batch_size
            area_count(nx, ny, batch_size) # 실무에서 슬라이싱 된 배열을 넣는 것보다, index를 넣는게 더 자주 사용된다고해서 사용
    
area_count(0, 0, N)

for i in [0, 1]:
    print(answer[i])
    