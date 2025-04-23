

T = int(input())   # 테스트 케이스 수

for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    visited = [False] * (N+1) # 1부터 시작하므로
    graph = [[] for _ in range(N+1)]

    for i in range(1, N+1):
        graph[i].append(P[i-1])   # 순열은 i → P[i-1]로 연결

    def dfs(node): # 한 노드에서 출발하고, 단방향이므로, 매개변수 줄음
        visited[node] = True
        for next in graph[node]:
            if not visited[next]:
                dfs(next)


    def dfs_stack(node):
        visited[node] = True
        stack = [node]

        while stack:
            next_node = stack.pop()
            for next in graph[next_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    stack.extend(graph[next_node])  # 순서를 맞추기 위해 역순으로 push
                    


    
    count = 0
    for i in range(1, N+1): # 사이클 개수 세는 코드
        if not visited[i]:
            dfs(i)
            count += 1

    print(count)
