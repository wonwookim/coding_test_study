# 	462276KB	2388ms
import sys
from collections import deque
# 전체 층, 현재 층, 목표 층, 올라가는 층, 내려가는 층
F, S, G, U, D = map(int, sys.stdin.readline().strip().split(' '))

visited = [False] * (F+1)

def make_graph(F,S,G,U,D,visited):
    if S == G:
        print(0)
        return
    que = deque()
    que.append((S,0)) # (1,0) 층과, 이동수 튜플
    graph = {}
    while que:
        pop1 = que.popleft() # (1,0)
        S = pop1[0]
        c = pop1[1]
        if visited[S] == False:
            visited[S] = True
            if S+U <= F:
                graph[S] = [(S+U,c+1)]
                if S+U == G:
                    print(graph[S][0][1])
                    return
            if S-D >0:
                if graph.get(S):
                    graph[S].append((S-D,c+1))
                else:
                    graph[pop1[0]] = [(S-D,c+1)]
                if S-D == G:
                    print(graph[S][0][1])
                    return
            if graph.get(S):
                que.extend(graph[S])
    print('use the stairs')
    return

make_graph(F,S,G,U,D,visited)

