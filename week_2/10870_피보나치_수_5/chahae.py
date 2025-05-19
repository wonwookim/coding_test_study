# 32412	32
N = int(input())

def F(N):
    if N > 1:
        return F(N - 1) + F(N - 2)
    elif N == 1:
        return 1
    else:
        return 0

print(F(N))
