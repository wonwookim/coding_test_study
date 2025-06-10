# 36700KB	128ms
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())

if K <= N:
    print(N - K)  # 뒤로만 가면 됨
else:
    visited = [False] * 100001
    que = deque()
    que.append((N, 0))
    visited[N] = True

    while que:
        pos, time = que.popleft()

        if pos == K:
            print(time)
            break

        # 넣을때 visited 검사 및 변경
        for next_pos in (pos - 1, pos + 1, pos * 2): # 이런식으로 해도 된다다
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                que.append((next_pos, time + 1))