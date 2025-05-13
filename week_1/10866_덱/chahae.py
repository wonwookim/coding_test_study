#시간:72ms 메모리:34936KB

import sys
from collections import deque

dq = deque()
input_ = sys.stdin.readline

N = int(input_())

for _ in range(N):
    command_list = input_().split()
    command = command_list[0]

    if command == "push_front":  # push_front X: 정수 X를 덱의 앞에 넣는다.
        X = int(command_list[1])
        dq.appendleft(X)
    elif command == "push_back":  # push_back X: 정수 X를 덱의 뒤에 넣는다.
        X = int(command_list[1])
        dq.append(X)
    elif command == "empty":  # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
        if not dq:
            print(1)
        else:
            print(0)
    elif command == "size":  # size: 덱에 들어있는 정수의 개수를 출력한다.
        print(len(dq))
    else:
        if not dq:  # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(-1)
        else:
            if command == "front":  # front: 덱의 가장 앞에 있는 정수를 출력한다.
                print(dq[0])
            elif command == "back":  # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
                print(dq[-1])
            elif command == "pop_front":  # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
                print(dq.popleft())
            elif command == "pop_back":  # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
                print(dq.pop())