# 32412KB	5284ms
import sys

N, S = map(int, sys.stdin.readline().strip().split()) # N 정수의 개수 S 정수
nums = list(map(int, sys.stdin.readline().strip().split())) # 정수들

# result = 0 이렇게하면 정수형은 immutable이기 때문에 함수내부에서 증가 시켜도 반영되지 않는다다
result = [0] # 결과값 세기

def back(N,M,start,listt,used,result):
    if len(listt) == M:
        if sum(listt) == S:
            result[0] +=1

    for i in range(start, N):
        if used[i] == False:
            used[i] = True
            listt.append(nums[i])
            back(N,M,i+1,listt,used,result)
            listt.pop()
            used[i] = False
            

for j in range(1,N+1):
    used = [False] * (N+1)
    back(N,j,0,[],used,result)

print(result[0])