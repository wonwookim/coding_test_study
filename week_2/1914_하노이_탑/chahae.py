# https://mgyo.tistory.com/185 참고
# 32412	800

import sys
N = int(sys.stdin.readline())

def hanoi(n, start, end, sub):
    if n == 1:
        print(start, end)
        return
    else :
        hanoi(n-1, start, sub, end)
        print(start, end)
        hanoi(n-1, sub, end, start)

print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)