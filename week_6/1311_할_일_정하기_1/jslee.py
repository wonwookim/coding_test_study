import sys
N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp[mask] = mask 상태까지 선택된 일들의 최소 위험도 합계, 계속 갱신
INF = float('inf')
dp = [INF] * (1 << N)
dp[0] = 0  # 아무 일도 하지 않은 상태

# 시간 초과때문에 이거 씀
bit_count = [0] * (1 << N)
for mask in range(1 << N):
    bit_count[mask] = bit_count[mask >> 1] + (mask & 1)

# 기존 코드에서 아래 줄 교체:
# person = bin(mask).count('1')


for mask in range(1 << N):
    person = bit_count[mask]  # 현재까지 배정된 사람 수, 문법은 처음 봄
    for j in range(N):  # j번 일
        if not (mask & (1 << j)):  # j번 일이 아직 선택되지 않았다면
            next_mask = mask | (1 << j) # 배당
            if dp[mask] == INF:
                continue
            dp[next_mask] = min(dp[next_mask], dp[mask] + cost[person][j]) # 비교

# 모든 일이 선택된 상태의 최소 비용 출력
print(dp[(1 << N) - 1])
