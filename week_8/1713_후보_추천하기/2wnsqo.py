# 32412KB	36ms
import sys

N = int(sys.stdin.readline().strip()) # 사진틀의 수
S = int(sys.stdin.readline().strip()) # 학생의 수
vote = list(map(int, sys.stdin.readline().strip().split())) # 투표 

vote_result = {}
c = 0
for i in range(len(vote)):
    if vote_result.get(vote[i]): # 사진이 있으면 
        vote_result[vote[i]][0] += 1 
    else: # 사진이 없으면
        if len(vote_result) < N: # 사진틀이 다 안찼으면 
            vote_result[vote[i]] = [1,c]
            c += 1
        else: # 사진틀이 다 찼으면
            # 투표수가 작은순 -> 오래된순 
            min_key = min(vote_result, key=lambda k: (vote_result[k][0],vote_result[k][1]))
            # 해당 key를 삭제
            del vote_result[min_key]

            # 사진틀 등록 
            vote_result[vote[i]] = [1,c]
            c +=1

result = sorted(vote_result.keys())

for j in range(len(result)):
    print(result[j], end=' ')