# 32412kb 36ms	

# 접근 방법 : 완전탐색

# 공집합 제외하고, 각 부분집합에 대해 신맛 곱 / 쓴맛 합 계산 후 |S - B| 최솟값 추적

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

for i in range(1, 1 << n):  # 공집합 제외
    s = 1  # 신맛 곱
    b = 0  # 쓴맛 합

    for j in range(n):
        if i & (1 << j):
            sour, bitter = arr[j]
            s *= sour
            b += bitter
                
    diff = abs(s - b)
    min_diff = min(min_diff, diff)

print(min_diff)
