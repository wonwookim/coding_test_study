import sys

input = sys.stdin.readline
write = sys.stdout.write

class goodSet:
    def __init__(self):
        self.s = set()

    def add(self, x):
        self.s.add(x)

    def remove(self, x):
        self.s.discard(x)

    def check(self, x):
        return 1 if x in self.s else 0

    def toggle(self, x):
        if x in self.s:
            self.s.remove(x)
        else:
            self.s.add(x)

    def all(self):
        self.s = set(range(1, 21))

    def empty(self):
        self.s.clear()

m = int(input())
b = goodSet()

for _ in range(m):
    cmd = input().strip().split()
    if cmd[0] == "add":
        b.add(int(cmd[1]))
    elif cmd[0] == "remove":
        b.remove(int(cmd[1]))
    elif cmd[0] == "check":
        write(str(b.check(int(cmd[1]))) + '\n')
    elif cmd[0] == "toggle":
        b.toggle(int(cmd[1]))
    elif cmd[0] == "all":
        b.all()
    elif cmd[0] == "empty":
        b.empty()
