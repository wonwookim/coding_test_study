#시간40ms  메모리 32412KB
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

#병든 기사는 오른쪽으로만 이동
#위/아래만 구분

#최대방문칸 = 이동횟수 + 1 

#세로길이가 1 : 움직일 수 없다. 즉, 시작 칸만 방문
if N == 1 :
    print(1)

#세로길이가 2 : 위/아래로 한 칸만 이동 가능
#경우의 수(위/아 1칸 오 2칸)
#이런 이동을 최대 (M-1)//2번 할 수 있다
elif N == 2:
    print(min(4, (M + 1) // 2))


#세로가 3 이상이면 위/아래 제약 없음
#가로가 7보다 작으면 4가지 방법 모두 쓸 수 없음(모두 쓰려면 최소 8칸)
elif N >= 3:
    if M < 7:
        print(min(4,M))
    else:
        print(M-2)

