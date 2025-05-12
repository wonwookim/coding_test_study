#시간:144ms 메모리:42360KB
# 문제잡고있는시간 잡아먹은 요인
# 1. 입력 값에 개행 ->?strip()
# 2. reverse() -> flag
# 3. 출력형식!!!! -> 공백때문에 그냥 출력 안됨. join사용
# 4. 뒤집어서 출력해주는거 잊어버림....

import sys
from collections import deque

input_ = sys.stdin.readline

T = int(input_())

for _ in range(T):
    flag = False
    command_list = input_().strip()
    _ = int(input_())
    num_str = input_().strip()
    if num_str == "[]":
        dq = deque()
    else:
        dq = deque(num_str.strip("[]").split(","))

    try:
        for c in command_list:
            if c == 'R':
                flag = not flag
            elif c == 'D':
                if flag:
                    dq.pop()
                else:
                    dq.popleft()
        if flag:
            dq.reverse()
            print(f"[{','.join(dq)}]")
        else :
            print(f"[{','.join(dq)}]")

    except IndexError:
        print("error")