# 45044KB	440ms
import sys
T = sys.stdin.readline().strip()
N_list = []
listt = []
for _ in range(int(T)):
    N_list.append(sys.stdin.readline().strip())
    listt.append(list(map(int, sys.stdin.readline().strip().split(' '))))

for i in range(int(T)): 
    dic = {}
    a = 0
    count = 0
    # 딕셔너리 작성
    for idx, l in enumerate(listt[i]):
        dic[idx+1] = l
    
    visited = [False] * (int(N_list[i]) + 1)

    for i in range(1, len(dic)+1):
        if visited[i] == False:
            visited[i] = True # 1 방문문
            a = dic[i] # 3 넣기 
            while 1:
                if visited[int(a)] == False:
                    visited[int(a)] = True
                    a = dic[int(a)]
                if a == i:
                    break
            count +=1
    print(count)



