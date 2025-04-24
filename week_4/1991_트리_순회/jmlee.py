#시간 32ms 메모리 32412KB
class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    @staticmethod
    def preorder(n):
        if n is not None:
            print(n.data, end='')
            Node.preorder(n.left)
            Node.preorder(n.right)
    @staticmethod
    def inorder(n):
        if n is not None:
            Node.inorder(n.left)
            print(n.data, end='')
            Node.inorder(n.right)
    @staticmethod
    def postorder(n):
        if n is not None:
            Node.postorder(n.left)
            Node.postorder(n.right)
            print(n.data, end='')

import sys
nodes = [line.strip().split() for line in sys.stdin.readlines()][1:]
#첫번째는 data, 두번째는 left, 세번째는 right
#.이면 None 처리

#1.이름 기반으로 노드 객체 먼저 생성
tree = {}
for data, left, right in nodes:
    tree[data] = Node(data)   

#2. left,right 문자열을 실제 객체로 연결
for data,left,right in nodes:
    tree[data].left = tree[left] if left != '.' else None
    tree[data].right = tree[right] if right != '.' else None

#3. 루트 노드에서 시작
root = tree[nodes[0][0]]


#4. 순회 실행
Node.preorder(root)
print()
Node.inorder(root)
print()
Node.postorder(root)