# 32412KB	32ms
import sys
n = int(sys.stdin.readline().strip())

def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(n))
