## 메모리 : 32412KB, 시간 : 36ms
import sys
N = int(sys.stdin.readline())
tree = {}
stack = []

for _ in range(N) :
    node, left, right = sys.stdin.readline().split()
    tree[node] = [left, right]

def preorder(node) :
    stack = [node]
    while len(stack) > 0 :
        current = stack.pop()
        print(current, end= '')
        if tree[current][1] != '.' :
            stack.append(tree[current][1])
        if tree[current][0] != '.' :
            stack.append(tree[current][0])
    return stack

def inorder(node) :
    stack = []
    current = node
    while len(stack) > 0 or current != '.' :
        if current != '.' :
            stack.append(current)
            current = tree[current][0]
        else :
            current = stack.pop()
            print(current, end='')
            current = tree[current][1]
    return stack

def postorder(node) :
    stack = [node]
    result = []
    while len(stack) > 0 :
        current = stack.pop()
        result.append(current)
        if tree[current][0] != '.' :
            stack.append(tree[current][0])
        if tree[current][1] != '.' :
            stack.append(tree[current][1])
    for node in reversed(result) :
        print(node, end='')
    return result

preorder(list(tree.keys())[0])
print('')
inorder(list(tree.keys())[0])
print('')
postorder(list(tree.keys())[0])