# 153720KB	3024ms
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    stock = list(map(int, sys.stdin.readline().strip().split()))

    max_price = 0
    result = 0
    # 뒤에서부터 탐색하는 이유 : 현재 가격이 max값 보다 작으면 사고 판다는 느낌으로 접근
    # 현재 가격이 max값보다 크면 어차피 손해 및 max값 갱신
    for i in range(N - 1, -1, -1):  # 뒤에서부터 탐색
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            result += max_price - stock[i]  # 지금 사서 max_price에 판다고 가정

    print(result)

# 시간초과과
# import sys

# T = int(sys.stdin.readline().strip()) # 테스트 케이스

# for _ in range(T):
#     N = int(sys.stdin.readline().strip()) # 날의 수
#     stock = list(map(int, sys.stdin.readline().strip().split())) # 날별 주가
#     result = 0
#     for i in range(N):
          # max(stock[i:])는 O(N) 시간이 걸린다 
#         if (max(stock[i:]) - stock[i]) > 0: # 지금 주가가 나중에 최대 수익이 + 라면면
#             result += max(stock[i:]) - stock[i]
    
#     print(result)