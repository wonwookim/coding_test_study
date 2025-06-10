# 145580	2164

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(tree - mid for tree in trees if tree > mid)

    if total >= M:
        result = mid  # 가능한 높이 중 최대
        start = mid + 1
    else:
        end = mid - 1

print(result)
