# 시간: 32ms, 메모리: 32412KB

# T : test case
# 각 줄마다 피보나치 함수에 넣을 파라미터 값(N은 40보다 작음)

# 잘못된 접근 -> 시간 초과
    # 1. 피보나치 함수를 만들기
    # 2. 조건을 이용
        # 1) n == 0일 때: 0 count를 담는 변수 + 1
        # 2) n == 1일 때: 1 count를 담는 변수 + 1
    # 3. 0의 count, 1의 count print하기

# 접근(dp)
    # 점화식 f(n) = f(n-1) + f(n-2) -> 자연수 n일 때, 0과 1의 개수 -> n-1일때의 0과 1의 개수 + n-2일때의 0과 1의 개수
    # 예외
        # n == 0 일때, 0의 개수: 1, 1의 개수: 0
        # n == 1 일때, 1의 개수: 0, 1의 개수: 1
    # for 구문을 통해 number가 2 이상인 경우 2부터  number까지 순회
    # 이미 방문 한 경험이 있으면 그냥 호출

    
import sys

input = sys.stdin.readline

T = int(input())

# key: 자연수, value: (0의 count, 1의 count)
counts = {0 : (1, 0),
          1 : (0, 1)}

for _ in range(T): # test case
    num = int(input())

    for i in range(num + 1): # dp (bottom-up)

        if counts.get(i, -1) == -1: # counts에 해당 자연수의 값이 없을 때 넣어주기
            (a,b),(c,d) = counts[i-2], counts[i-1] # 점화식
            counts[i] = a + c, b + d

    print(' '.join(map(str,counts[num])))


