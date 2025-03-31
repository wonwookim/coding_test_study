import sys

class Deque:
    def __init__(self):
        self.data = []

    def push_front(self, x):
        self.data.insert(0, x)

    def push_back(self, x):
        self.data.append(x)

    def pop_front(self):
        return self.data.pop(0) if self.data else -1

    def pop_back(self):
        return self.data.pop() if self.data else -1

    def size(self):
        return len(self.data)

    def empty(self):
        return 1 if not self.data else 0

    def front(self):
        return self.data[0] if self.data else -1

    def back(self):
        return self.data[-1] if self.data else -1

# 입력 전체 받아오기
input = sys.stdin.readlines
commands = input()

dq = Deque()
output = []

for cmd in commands[1:]:  # 첫 줄은 명령 개수 (무시)
    cmd = cmd.strip()
    if cmd.startswith("push_front"):
        _, x = cmd.split()
        dq.push_front(int(x))
    elif cmd.startswith("push_back"):
        _, x = cmd.split()
        dq.push_back(int(x))
    elif cmd == "pop_front":
        output.append(str(dq.pop_front()))
    elif cmd == "pop_back":
        output.append(str(dq.pop_back()))
    elif cmd == "size":
        output.append(str(dq.size()))
    elif cmd == "empty":
        output.append(str(dq.empty()))
    elif cmd == "front":
        output.append(str(dq.front()))
    elif cmd == "back":
        output.append(str(dq.back()))

# 출력 한 번에 처리
print('\n'.join(output))
