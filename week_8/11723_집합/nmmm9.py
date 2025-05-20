# 32412kb	3428ms
import sys
input = sys.stdin.readline

M = int(input())
S = 0  

for _ in range(M):
    cmd = input().strip().split()

    if cmd[0] == 'add':
        x = int(cmd[1])
        S |= (1 << (x - 1))  # x번째 비트를 1로 설정

    elif cmd[0] == 'remove':
        x = int(cmd[1])
        S &= ~(1 << (x - 1))  # x번째 비트를 0으로 설정

    elif cmd[0] == 'check':
        x = int(cmd[1])
        print(1 if S & (1 << (x - 1)) else 0)  # x번째 비트가 1이면 1, 아니면 0 출력

    elif cmd[0] == 'toggle':
        x = int(cmd[1])
        S ^= (1 << (x - 1))  # x번째 비트를 반전 (1 -> 0, 0 -> 1)

    elif cmd[0] == 'all':
        S = (1 << 20) - 1  # 20개의 비트를 전부 1로 설정

    elif cmd[0] == 'empty':
        S = 0  # 모두 제거
