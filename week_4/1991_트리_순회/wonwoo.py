# 시간 : 60ms, 메모리 : 34976 KB
# 첫째줄 : N (노드 개수)
# 두번째줄 : 노드, 왼쪽 자식, 오른쪽 자식

# 접근
    # 그래프 생성
    # 전위 : dfs
    # 중위 : 재귀,,?
    # 후위 : 재귀,,?

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = {}
preorder_result = []
inorder_result = []
postorder_result = []


for _ in range(N): # 그래프 생성
    node, l_cn, r_cn = input().strip().split()
    graph[node] = [l_cn, r_cn]


def preorder_traverse(graph, node, visited): # 전위 영어래요,, ㅎㅎ, dfs
    if node in visited:
        return None
    global preorder_result
    visited.add(node)
    preorder_result.append(node)
    for child_node in graph[node]:
        if child_node != '.':
            preorder_traverse(graph, child_node, visited)
    

def inorder_traverse(graph, node): # 중위
    if node in '.':
        return None
    global inorder_result
    inorder_traverse(graph, graph[node][0])
    inorder_result.append(node)
    inorder_traverse(graph, graph[node][1])

def postorder_traverse(graph, node): # 후위
    if node in '.':
        return None
    global postorder_result
    postorder_traverse(graph, graph[node][0])
    postorder_traverse(graph, graph[node][1])
    postorder_result.append(node)

preorder_traverse(graph, next(iter(graph)), set()) # next(iter()) -> key 요소 한개씩 가져옴
print(''.join(preorder_result))

inorder_traverse(graph, next(iter(graph)))
print(''.join(inorder_result))

postorder_traverse(graph, next(iter(graph)))
print(''.join(postorder_result))