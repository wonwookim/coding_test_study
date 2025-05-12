#시간:44ms 메모리:33432KB

import sys

N = int(sys.stdin.readline())
my_stack = []

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        my_stack.append(int(command[1]))
    elif command[0] == 'pop':
        print(my_stack.pop() if my_stack else -1)
    elif command[0] == 'size':
        print(len(my_stack))
    elif command[0] == 'empty':
        print(0 if my_stack else 1)
    elif command[0] == 'top':
        print(my_stack[-1] if my_stack else -1)