import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def is_same(paper, x, y, size):
    base = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != base:
                return False
    return True

count = [0,0,0] #각각 -1, 0 ,1 개수 저장


def divide_and_conquer(x, y, size):
    if is_same(paper, x, y, size):
        count[paper[x][y] + 1] += 1  # -1 → 0, 0 → 1, 1 → 2 변환해서 저장
        return
    new_size = size // 3
    for i in range(3): # 종이가 9개니 3x3으로 쪼개기.
        for j in range(3):
            divide_and_conquer(x + i * new_size, y + j * new_size, new_size)


divide_and_conquer(0,0,N)
print(count[0])
print(count[1])
print(count[2])
