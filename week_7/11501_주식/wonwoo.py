# 시간: 3308ms, 메모리: 159996KB
# T : test case 개수, N : 일별 주가
# 잘못된 접근 
    # max, min 값 구하기
    # for 구문 이용
        # 해당 값이 max보다 작으면 구매
        # 해당 값이 max면 판매
    # max값일 때 무조건 판매를 했는데, 그러면 마지막에 max값이 아니여서 못 팔게 되는 경우 존재
# 접근
    # list 뒤집기
    # max_price = 0
    # reverse_days for 구문 이용
    # max_price보다 값이 크면 max_price 갱신
    # max_price와 같으면 아무런 행동도 안 함
    # max_price보다 값이 작으면 차익 생김
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int,input().split()))

    profit = 0
    max_price = 0
    
    for day in days[::-1]:
        if day > max_price :
            max_price = day
        elif day < max_price:
            day_profit = max_price - day
            profit += day_profit

    print(profit)
