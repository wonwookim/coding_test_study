# N개의 물건, 각 물건은 무게 W와 가치 V를 가짐, V만큼 즐길 수 있음
# 최대 K만큼의 무게만을 넣을 수 있는 배낭
# 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
# 입력: 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
# 입력으로 주어지는 모든 수는 정수
# 출력: 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 한 줄에 출력

# 메모리 228328KB, 시간 5896ms
# 참고 링크
# https://sjkoding.tistory.com/99
# https://beyond-common-sense.tistory.com/4
# 추가로 학습하면 좋은 문항: 2758번 로또, 1106번 호텔

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
item = []
for _ in range(N):
    W, V = map(int, input().strip().split())
    item.append((W, V))

dp = [[0] * (K+1) for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(1, K+1):
        dp[0][k] = 0 # 물건을 하나도 담지 않음, 버틸 수 있는 무게는 K, 가치는 0

        if item[n-1][0] > k: # 물건의 무게가 버틸 수 있는 무게보다 큰 경우
            dp[n][k] = dp[n-1][k] # 물건을 선택하지 않음 -> 버틸 수 있는 무게는 전과 동일
        else: # 물건의 무게가 버틸 수 있는 무게보다 작은 경우 (즉, 물건을 고를 수 있는 상황)
            dp[n][k] = max(dp[n-1][k], # 물건을 선택하지 않음 -> 버틸 수 있는 무게는 전과 동일
                           dp[n-1][k-item[n-1][0]] + item[n-1][1]) # 물건을 선택 -> 버틸 수 있는 무게는 줄어들고, 가치는 늘어남
print(dp[-1][-1])