# 32412KB	32ms
# 34992KB	56ms
import sys
# from collections import deque
N = sys.stdin.readline().strip()
graph = {}
for _ in range(int(N)):
    a, b, c = sys.stdin.readline().strip().split(' ')
    graph[a] = [b,c]

# print(graph)

# def front(graph, start):
#     lque = deque()
#     rque = deque()
#     print(start, end="")
#     lque.append(graph[start][0])
#     rque.append(graph[start][1])
#     if lque[0] != '.':
#         front(graph, lque[0])
#         lque.popleft()
#     if rque[0] != '.':
#         front(graph, rque[0])
#         rque.popleft()
def front(graph, start):
    print(start, end="")
    if graph[start][0] != '.':
        front(graph,graph[start][0])
    if graph[start][1] != '.':
        front(graph,graph[start][1])
    return


front(graph, 'A')
print()

def middle(graph,start):
    if graph[start][0] != '.':
        middle(graph,graph[start][0])
    print(start, end="")
    if graph[start][1] != '.':
        middle(graph,graph[start][1])
    return

middle(graph,'A')
print()

def back(graph,start):
    if graph[start][0] != '.':
        back(graph,graph[start][0])
    
    if graph[start][1] != '.':
        back(graph,graph[start][1])

    print(start, end="")
    return

back(graph,'A')