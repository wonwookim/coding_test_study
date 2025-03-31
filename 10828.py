class Stack:
    def __init__(self):
        self.mystack = []

    def push(self, X):
        self.mystack.append(X)

    def pop(self):
        if self.mystack:
            tmp = self.mystack.pop()
            print(tmp)
        else:
            print(-1)

    def size(self):
        print(len(self.mystack))

    def empty(self):
        if self.mystack:
            print(0)
        else:
            print(1)

    def top(self):
        if self.mystack:
            print(self.mystack[-1])
        else:
            print(-1)


stack1 = Stack()
N = int(input())
for _ in range(N):
    command = input().split()
    if command[0] == "push":
        stack1.push(int(command[1]))
    elif command[0] == "pop":
        stack1.pop()
    elif command[0] == "top":
        stack1.top()
    elif command[0] == "size":
        stack1.size()
    elif command[0] == "empty":
        stack1.empty()
