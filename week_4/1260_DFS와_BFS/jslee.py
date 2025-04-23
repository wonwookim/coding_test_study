
N = int(input())
tree = dict()

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(tree, node):
    if node == '.':      # 자식 루트 없는 것 판별
        return
    left, right = tree[node]        # ← 언패킹. left와 right를 분배함
    print(node, end='')
    preorder(tree, left)
    preorder(tree, right)

def inorder(tree, node):
    if node == '.':      
        return
    left, right = tree[node]        
    inorder(tree, left)
    print(node, end='')
    inorder(tree, right)

def postorder(tree, node):
    if node == '.':   
        return
    left, right = tree[node]       
    postorder(tree, left)
    postorder(tree, right)
    print(node, end='')
    

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
