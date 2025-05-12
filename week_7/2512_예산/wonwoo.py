# 시간: 48ms, 메모리: 33432KB

# N: 지방의 수, M: 총 예산
# 접근
    # 최대 예산 = max()
    # 1 부터 최대 예산 사이의 값을 이분 탐색으로 찾기
    # 예산의 중앙값 찾기
    # 만약 해당 값이 예산의 중앙값보다 작으면 그냥 더하기  
    # 크면 예산의 중앙값을 더하기
    # 다 더한 값이 총 예산보다 적을 경우 시작 값을 중앙값 + 1로 설정하고 다시 돌기
    # 더 높을 경우 최대 예산을 중앙값 -1 로 설정하고 다시 돌기

import sys
input = sys.stdin.readline

N = int(input())
countries = list(map(int, input().split()))
total_budget = int(input())

start = 1
end = max(countries)
budget = 0

while start <= end:
    mid = (start+end) // 2
    estimate_budget = sum([min(country, mid) for country in countries]) 

    if estimate_budget <= total_budget:
        start = mid + 1 # 예산을 mid보다 더 높여도 되니 +1 함
        budget = mid

    else:
        end = mid - 1 # 예산을 mid보다 더 낮춰야하니 -1

print(budget)