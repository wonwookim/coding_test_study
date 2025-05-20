# 그냥 전부다 만들어서 합을 확인 >> 대신 비트마스킹 사용
# 32412kb    3332ms

n, s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0  

for i in range(1, 1 << n):  # 1 << N: 2의 n제곱, 1부터 시작하여 공집합 제외
    subset_sum = 0  
    for j in range(n):  
        if i & (1 << j):    # i의 j번째 비트가 1이면 → j번째 원소 포함
            subset_sum += nums[j]

    if subset_sum == s:  # 부분수열의 합이 S와 같으면 cnt 증가
        cnt += 1

print(cnt)
