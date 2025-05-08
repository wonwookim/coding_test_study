import sys
input = sys.stdin.readline

N = int(input().strip())
paper = [list(map(int, input().strip())) for _ in range(N)]



# 괄호 실패
#def is_same(paper, x, y, size):
#    base = paper[x][y]
#    for i in range(x, x + size):
#       for j in range(y, y + size):
#            if paper[i][j] != base:
#                return False
#    if base == 0:
#        print(0)
#    elif base == 1:
#        print(1)
#    return True


# def divide_and_conquer(x, y, size):
#    if is_same(paper, x, y, size):
#        return
#    new_size = size // 2
#    for i in range(2): # 종이 2x2으로 쪼개기.
#        for j in range(2):
#            divide_and_conquer(x + i * new_size, y + j * new_size, new_size)


# divide_and_conquer(0,0,N)




def is_same(paper, x, y, size):
    base = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != base:
                return False
    return True

def divide_and_conquer(x, y, size):
    if is_same(paper, x, y, size):
        return str(paper[x][y])
    new_size = size // 2
    result = "("
    for i in range(2):
        for j in range(2):
            result += divide_and_conquer(x + i * new_size, y + j * new_size, new_size)
    result += ")"
    return result


print(divide_and_conquer(0, 0, N))



