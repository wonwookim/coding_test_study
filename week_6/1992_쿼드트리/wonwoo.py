# 시간: 36ms, 메모리: 32412KB
# N: 영상의 크기 (1 ~ 64)
# 최대 시간복잡도 : 6 * 64 * 64 = 24,576 -> 좀 다른듯
# 접근:
    # 재귀함수 사용
    # for를 이용하여 값이 모두 같은지 확인
    # 값이 다른 경우 4등분하여 재귀함수 진행
    # 값이 같은 경우 0 or 1 표출
import sys
input = sys.stdin.readline

N = int(input())

quad_tree = [list(input().strip()) for _ in range(N)]
def compression(x, y, n):
    answer = ''
    key = quad_tree[y][x]
    is_same = True
    for ny in range(y, y + n):
        for nx in range(x, x + n):
            if key != quad_tree[ny][nx]:
                is_same = False
                break
        if not is_same:
            break
    
    if is_same:
        return key # 같은 경우 key만 출력
    
    batch_size = n // 2
    for ny in range(0, 2):
        for nx in range(0, 2):
            dy = y + (ny * batch_size)
            dx = x + (nx * batch_size)
            answer += f'{compression(dx, dy, batch_size)}'
    return f'({answer})' # 다 끝났을 경우 ()를 씌워서 보여주기

print(compression(0, 0, N))