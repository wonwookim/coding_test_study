# 32412KB	36ms
import sys

N = int(sys.stdin.readline().strip())
food = [] # 재료 리스트(신맛, 쓴맛맛)
for _ in range(N):
    S, B = map(int, sys.stdin.readline().strip().split())
    food.append((S,B))

result = [] # 조합별 결과를 담을 리스트

def backtrack(N,M,dish,start,used ,result):
    if len(dish) == M: # 재료를 다 골랐으면 
        s, b = 1,0
        for t in range(M):
            s = s * dish[t][0]
            b = b + dish[t][1]
            result.append(abs(s-b)) # 결과 저장장
            # return
    for j in range(start,N):
        if used[j] == False:
            used[j] = True
            dish.append(food[j])
            backtrack(N,M,dish,j+1,used ,result) # start j+1 앞에 사용했던 인덱스 안쓰기기
            dish.pop() # 백트래킹
            used[j] = False

for M in range(1,N+1): # 재료를 1개부터 N개 선택
    used = [False] * (N+1) # 사용했는지 확인하는 리스트트
    backtrack(N,M,[], 0,used ,result) # start 값을 넘겨주어야 한다 아니면 (1,2) (2,1) 중복 사용용

print(min(result))


