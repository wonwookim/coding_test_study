# 33432KB	52ms
import sys

N = int(sys.stdin.readline().strip()) # 지방의 수
budget = list(map(int, sys.stdin.readline().strip().split())) # 지방별 예산요청
M = int(sys.stdin.readline().strip()) # 총 예산

budget_sum = 0

for i in range(N):
    budget_sum += budget[i] # 예산 합계 계산

if M == N: # 지방수와 예산이 같으면
    print(1)
elif M >= budget_sum: # 모든 지방의 예산을 지원해도 총 예산을 넘지 않을 경우
    print(max(budget))

else:
    start = 0
    end = max(budget)
    result = 0

    while start <= end:
        mid = (start + end) // 2 # 이진탐색을 위해 중간값 선택
        # 중간값 보다 작으면 사용 아니면 중간값 사용으로 합계 구하기
        total = sum(min(b, mid) for b in budget)

        if total <= M: 
            result = mid  # 가능한 상한값 저장
            start = mid + 1 # 더 수용가능하므로 start를 증가시켜 mid를 올린다
        else:
            end = mid - 1 # 수용이 불가능 하므로 end를 내린다 

        # +- 1 을 하는 이유는 한번 본 mid는 보지 않기 위해서

    print(result)
        
