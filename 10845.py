class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedQueue:
    def __init__(self):
        self.head = None  # front
        self.tail = None  # back
        self.count = 0

    def push(self, x):
        new_node = Node(x)
        if not self.head:  # 큐가 비어있는 경우
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def pop(self):
        if not self.head:
            print(-1)
            return
        print(self.head.data)
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  # 비게 되었을 경우
        self.count -= 1

    def size(self):
        print(self.count)

    def empty(self):
        print(1 if self.count == 0 else 0)

    def front(self):
        if not self.head:
            print(-1)
        else:
            print(self.head.data)

    def back(self):
        if not self.tail:
            print(-1)
        else:
            print(self.tail.data)


DoubleLinkedQueue1 = DoubleLinkedQueue()
N = int(input())
for _ in range(N):
    command = input().split()
    if command[0] == "push":
        DoubleLinkedQueue1.push(int(command[1]))
    elif command[0] == "pop":
        DoubleLinkedQueue1.pop()
    elif command[0] == "front":
        DoubleLinkedQueue1.front()
    elif command[0] == "back":
        DoubleLinkedQueue1.back()
    elif command[0] == "size":
        DoubleLinkedQueue1.size()
    elif command[0] == "empty":
        DoubleLinkedQueue1.empty()
