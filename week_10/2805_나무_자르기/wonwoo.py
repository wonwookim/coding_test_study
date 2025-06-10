# 시간: 2064ms, 메모리: 148224KB

# N: 나무의 수, M: 집에 가져갈 나무의 길이  (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

# 접근:
    # 절단기에 설정하는 높이에 대한 이분탐색
    # 범위: 0 ~ 나무들의 최대 높이
    # 잘랐을 때, 
    # 가져갈 수 있는 길이의 합이 
    #   M보다 크면 가운데보다 높은 범위
    #   M보다 작으면 가운데보다 작은 범위
    #   M과 같으면 스탑

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

trees = list(map(int,input().split()))

max_length = max(trees)
height = max_length // 2 # 이분탐색 초기 값: 나무들의 최대 높이의 절반


def find_cut_height(m, trees):
    lo, hi = 0, max(trees)
    answer = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        # mid 높이로 잘랐을 때 얻는 나무 길이 합
        cut_sum = sum(tree - mid for tree in trees if tree > mid)
        
        if cut_sum < m:
            # 너무 적게 잘림 → 절단기를 더 낮춰야 함
            hi = mid - 1
        else:
            # M 이상 잘렸으므로, 이 높이는 유효한 후보
            answer = mid
            # 더 높은 절단 높이를 시도해 봄
            lo = mid + 1

    return answer

print(find_cut_height(M, trees))