# 38300KB	104ms
import sys
N, M = map(int, sys.stdin.readline().strip().split())

name = {}
result = []
for i in range(N+M):
    if i <= (N-1): # 듣도 보도 못한 사람은 리스트에 담기 
        name[sys.stdin.readline().strip()] = 1
    else: # 보도 못한 사람은 비교하기 
        person = sys.stdin.readline().strip()
        if name.get(person):
            result.append(person)

result.sort()
print(len(result))
print(*result, sep='\n') # 가독성이 떨어지지만 for문보다 빠르다 

