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

count = [0,0] #각각 0 ,1 개수 저장


def divide_and_conquer(x, y, size):
    if is_same(paper, x, y, size):
        count[paper[x][y]] += 1
        return
    new_size = size // 2
    for i in range(2): # 종이 2x2으로 쪼개기.
        for j in range(2):
            divide_and_conquer(x + i * new_size, y + j * new_size, new_size)


divide_and_conquer(0,0,N)
print(count[0])
print(count[1])


