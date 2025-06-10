## 메모리 : 32142 KB, 시간 : 44 ms
import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    N = int(sys.stdin.readline())

    fib = [[0, 0] for _ in range(41)]
    fib[0] = [1, 0]
    fib[1] = [0, 1]
    
    for i in range(2, 41) :
        fib[i][0] = fib[i-1][0] + fib[i-2][0]
        fib[i][1] = fib[i-1][1] + fib[i-2][1]
    
    print(' '.join(str(num) for num in fib[N]))
