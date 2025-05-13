import sys
from itertools import combinations
input = sys.stdin.readline

N, C = map(int, input().split())
#적은 순서대로 정렬(이진탐색 전제조건)
houses = sorted(int(input()) for _ in range(N))

#이진탐색 + 그리디 : 최소 거리의 최댓값
#공유기 사이의 거리를 d라고 했을 때, 최소 거리 d로 공유기를 C개 이상 설치할 수 있는가?
def routers(min_dist):
    count = 1 #첫번째 집(=last)는 설치한다고 가정
    last = houses[0]
    #두번째 집부터 순회
    for i in range(1, N):
        if houses[i] - last >= min_dist:
            count += 1
            last = houses[i]
    # 공유기를 C개 이상 설치 가능
    return count >= C

#이진탐색 초기 범위
low = 1 #최소거리의 최솟값
high = houses[-1] - houses[0] #가능한 최대 거리(양 끝)
result = 0 #정답(최소거리의 최댓값)

#이진탐색 수행
while low <= high:
    mid = (low + high) // 2
    if routers(mid):
        # 공유기 C개 설치 가능하면 일단 저장
        # 거리 늘리기(더 멀리도 설치 가능한가?)
        result = mid
        low = mid + 1
    else:
        # 공유기 C개 설치 불가능 -> 너무 멀리 벌림
        # 거리 줄이기
        high = mid - 1

print(result)



# 처음에 완전탐색으로 시도해서 시간초과 발생 
# max_min_dist = 0
# for comb in combinations(matrix, C):  # 이건 제너레이터라 메모리 걱정 없음
#     # 조합에서 모든 두 수 간 거리 중 최소값 구하기
#     min_dist = float('inf')
#     for i in range(C):
#         for j in range(i + 1, C):
#             dist = abs(comb[i] - comb[j])
#             min_dist = min(min_dist, dist)
#     max_min_dist = max(max_min_dist, min_dist)

# print(max_min_dist)
