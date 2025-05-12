#시간:44ms 메모리:33432KB

import sys

N = int(sys.stdin.readline())
my_queue = []

for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        my_queue.append(int(command[1]))
    elif command[0] == 'pop':
        print(my_queue.pop(0) if my_queue else -1)
    elif command[0] == 'size':
        print(len(my_queue))
    elif command[0] == 'empty':
        print(0 if my_queue else 1)
    elif command[0] == 'front':
        print(my_queue[0] if my_queue else -1)
    elif command[0] == 'back':
        print(my_queue[-1] if my_queue else -1)

