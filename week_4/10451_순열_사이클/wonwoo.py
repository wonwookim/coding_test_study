# 428ms, 33432KB
# T: testcase, N : 순열의 크기

# 접근 :
    # dict 생성 : 1~N이라는 key, 그에 맞는 value 
    # 1~N까지 반복문 돌며
        # dfs를 이용하여 물고 들어가는 형식
        # 방문하였으면 빠져나오기

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())



for _ in range(T):
    N = int(input())
    value = list(map(int, input().strip().split())) # 순열
    graph = dict(zip([i for i in range(1, N + 1)], value)) # 그래프 생성

    current_key = 0
    visited = set() # 방문 여부
    group_dict = {}

    def dfs(node, current_set): # 재귀함수 이용
        if node in visited:
            return None
        visited.add(node) # 방문 여부 추가
        current_set.add(node)
        dfs(graph[node], current_set) # key가 node인 value를 넣어서 dfs 재귀 진행
        return None

    for node in graph.values():
        if node not in visited:
            current_set = set()
            dfs(node, current_set)
            group_dict[current_key] = current_set
            current_key += 1 # dict의 key 값을 관리하기 위함 -> 순열 사이클 개수수

    print(len(group_dict))

    

