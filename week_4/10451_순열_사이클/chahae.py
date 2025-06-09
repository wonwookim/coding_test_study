# 32412	448
# T: 테스트케이스의 수 
# N: 각 테스트케이스의 수

import sys
input_ = sys.stdin.readline
T = int(input_())


for _ in range(T):
    visited = set()
    graph = {}
    stack = []
    cnt = 0

    N = int(input_())
    arr = list(map(int, input_().split()))
    for i in range(1, N+1):
        graph[i] = arr[i-1]
    
    for i in range(1, N+1):
        if i not in visited:
            stack.append(i)
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.append(graph[node])
                else:
                    cnt += 1
                    break

    print(cnt)