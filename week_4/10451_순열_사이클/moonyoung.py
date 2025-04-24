## 메모리 : 32412KB, 시간 : 264ms
import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    count = 0
    N = int(sys.stdin.readline())
    visited = [False] * (N + 1)
    # 인덱스 1부터 활용할 것이기 때문에 [0]을 붙여서 인덱스를 밀리게함함
    permutation = [0] + list(map(int, sys.stdin.readline().split()))
    for i in range(1, N + 1) :
        if visited[i] == False :
            current = i
            while visited[current] == False :
                visited[current] = True
                current = permutation[current]
            count += 1
    print(count)



