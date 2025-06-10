## 메모리 : 159304 KB, 시간 : 1816 ms
import sys
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

index_X = sorted(set(X))

dict = {}
for idx, value in enumerate(index_X) :
    dict[value] = idx

for value in X :
    print(dict[value], end=' ')