N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

count = float('inf')
for mask in range(1, 1 << N):
    S_count = 1
    B_count = 0
    for i in range(N):
        if mask & (1 << i):
            S_count *= lst[i][0]
            B_count += lst[i][1]
    count = min(count, abs(S_count - B_count))

print(count)
