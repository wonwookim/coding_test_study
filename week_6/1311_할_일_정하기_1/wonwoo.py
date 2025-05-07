# 점화식 : 
    # dp[person][mask] = min(dp[person][mask], [person-1][prev_mask] + cost[person][j]) -> 기존에 mask를 사용하지 않고 풀었을 경우 x 

# 비트마스킹을 이용하는 이유 -> 메모리 및 시간 단축
# 비트마스킹 문제 쉬운 것 좀 풀어봐야 할 것 같음
# 비트마스킹을 이용해서 푸는 방식 완전히 이해 x

import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이를 늘려주는 것
input = sys.stdin.readline
N = int(input())
array = [list(map(int,input().strip().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for _ in range(N)]# N개의 bit 생성 -> (1<<N) 이 때 N이 3이면 8개 생성이 되는 것 -> 3개의 일에 배정 될 경우의 수 8개

def dfs(person, mask):
    if person == N:
        return 0  # 모든 사람에게 일 배정 완료
    if dp[person][mask] != -1:
        return dp[person][mask] # -1이 아니면 이미 배정 된 경우

    min_cost = float('inf')
    for job in range(N): # 맨 처음일 경우 첫번째 사람에게 3가지의 일을 배정하는 모든 경우의 수 확인
        if not (mask & (1 << job)):  # 아직 배정되지 않은 일, job이 0일 경우 (1 << job)은 001, 1일 경우 010
            # mask와 그 값이 동시에 1이라면 해당 일은 배정 받은 경우로 pass
            new_mask = mask | (1 << job) # mask가 000, job이 0인 경우 -> new_mask = 001 -> 1번 일을 배정 받은 것 
            total_cost = array[person][job] + dfs(person + 1, new_mask) # 점화식을 이용(mask를 초기화)
            min_cost = min(min_cost, total_cost) # 첫번째 사람에게 각각의 일을 배정 받았을 때, 최소 값을 확인

    dp[person][mask] = min_cost # 최종 최솟값을 해당 person에게 지정하기기
    return min_cost

print(dfs(0, 0))
