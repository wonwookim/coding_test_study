## 시간 : 148224 KB, 4968 ms
# 이분 탐색
import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(trees)

while low <= high :
    mid = (low + high) // 2
    cut_tree = 0

    for tree in trees :
        if tree > mid :
            cut_tree += (tree - mid)
    
    if cut_tree >= M :
        low = mid + 1
    else :
        high = mid - 1

print(high)