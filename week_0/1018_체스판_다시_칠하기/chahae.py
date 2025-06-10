# 체스판칠하기
# 32412	64

import sys
input = sys.stdin.readline

# N X M
# 체스 색 정보 (W or B)
N, M = map(int, input().split())
min_cnt = 33
# 최소수정횟수 변수선언
# 최소수정횟수 변수 33으로 선언

# 한판넣을변수선언 체스 = 8*8 리스트 
input_C = []
# 2차원리스트로 입력 받기( 라인 M번 반복 )
for i in range(N):
    row_ = input()
    input_C.append(list(row_))


# 한 판 확인 할 사용자함수

#def check(check_C):
#    cnt = 0
#    for i in range(8):
#        for j in range(8):
#            if ((i%2 == 0) and (j%2==0)) or ((i%2 != 0) and (j%2 !=0)):
#                if check_C[i+x][j+y] != "B" :
#                    cnt +=1
#            else :
#                if check_C[i+x][j+y] != "W" :
#                    cnt +=1
#    if cnt > 32:
#        return 64-cnt
#    else:
#        return cnt

# 무조건 [0][0]을 B라고 가정하고 진행(64-여기서 나온 수정횟수 -> W일때 수정횟수)
# 행인덱스가 짝수이면서 열인덱스가 짝수 일때 B가 아니면 카운드 +1
# 행인덱스가 홀수이면서 열인덱스가 홀수 일때 B가 아니면 카운드 +1
# 그외에 W가 아니면 카운드 +1
# 수정횟수가 32보다 크면 64-수정횟수 해줘서 리턴
# 수정횟수가 32이하이면 그대로 리턴


# (N - 7)번  ,  (M - 7)번 나눠서

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for x in range(8):
            for y in range(8):
                if ((x+y)%2 == 0):
                    if input_C[i+x][j+y] != "B" :
                        cnt +=1
                else :
                    if input_C[i+x][j+y] != "W" :
                        cnt +=1
        if cnt > 32:
            cnt = 64-cnt
        
        if min_cnt > cnt:
            min_cnt = cnt 

print(min_cnt)