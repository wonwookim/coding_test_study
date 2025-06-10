# 145580KB	2160ms
import sys
inputs = sys.stdin.readline
N, M = map(int, input().split()) # 나무 수, 높이
tree = list(map(int, input().split()))

start = 0
end = max(tree)
mid = 0
result = 0
while start <= end:
    mid = (start+end)//2
    out_put= sum(t - mid for t in tree if t > mid)

    if out_put >= M:
        result = mid # 이렇게 계속 저장해야 원하는 나무 길이와 다르더라도 최대값을 저장 할 수 있다.
        start = mid + 1
    else:
        end = mid - 1

print(result)