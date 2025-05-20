# 시간: 3100ms, 메모리: 32412KB

import sys
input = sys.stdin.readline

M = int(input())
S = 0 # 공집합

for _ in range(M):
    temp = input().strip().split(' ')
    
    if temp[0] == 'add':
        S |= (1<<int(temp[1])) # num번째에다가 1을 넣겠다.
    elif temp[0] == 'remove':
        S &= ~(1<<int(temp[1]))
    elif temp[0] == 'check':
        print(1 if S & (1<<int(temp[1])) else 0)
    elif temp[0] == 'toggle':
        S ^= (1<<int(temp[1]))
    elif temp[0] == 'all':
        S = (1<< 21) - 1
    elif temp[0] == 'empty':
        S = 0