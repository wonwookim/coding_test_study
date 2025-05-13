#시간 3488ms  메모리 153708KB
T = int(input())

for _ in range(T):
    days = int(input())

    price_list = list(map(int, input().split()))
    
    max_price = 0
    total_profit = 0

    # 주가를 뒤에서부터 하나씩 보기 (나중 날부터 앞으로)
    for i in range(len(price_list) - 1, -1, -1):
        today_price = price_list[i]  # 오늘 주가

        # 만약 오늘 주가가 지금까지 본 주가 중 최고가보다 높다면
        if today_price > max_price:
            max_price = today_price  # 최고가를 갱신함
        else:
            # 오늘 주가가 최고가보다 작으면,
            # 오늘 주식을 사서 최고가에 판다고 가정하고 이익 계산
            profit = max_price - today_price
            total_profit += profit

    # 이 테스트케이스에서의 총 이익 출력
    print(total_profit)
