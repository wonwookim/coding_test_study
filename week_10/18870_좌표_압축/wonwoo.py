# 시간: 1356ms, 메모리: 189600KB

# N : 좌표 개수 (1 ≤ N ≤ 1,000,000)
# X1, X2, ..., XN (-10^9 ≤ Xi ≤ 10^9)

# 접근:
    # set을 하고 sort
    # 바텀업 방식으로 f(n) = f(n-1) + 1 (n: n번쨰 좌표)

import sys
input = sys.stdin.readline

N = int(input())

axis = list(map(int, input().split()))
set_axis = list(set(axis))
set_axis.sort()

a = {axis: (idx) for idx, axis in enumerate(set_axis)}

answer = list(map(str,[a.get(ax) for ax in axis]))
print(' '.join(answer))

    
