#시간 52ms  메모리 33432KB
n = int(input())

budget_list = list(map(int, input().split()))

total_budget = int(input())

low = 0
high = max(budget_list)

answer = 0

while low <= high:
    mid = (low + high) // 2  # 상한액 후보

    # 상한액을 기준으로 실제 배정할 예산 계산
    temp_total = 0
    for b in budget_list:
        if b > mid:
            temp_total += mid  # 상한 넘으면 상한액만 줌
        else:
            temp_total += b    # 상한 안 넘으면 그대로 줌

    # 총합이 예산 안 넘으면 더 크게 줄 수 있음
    if temp_total <= total_budget:
        answer = mid           # 지금 상한액 저장해두고
        low = mid + 1          # 더 큰 상한액도 가능한지 봄
    else:
        high = mid - 1         # 예산 초과 → 상한액 줄여야 함

# 최종 결정된 상한액 출력
print(answer)
