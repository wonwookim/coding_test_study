#시간 296ms, 메모리 41144KB
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int,(input().split())))

# 누적합이 아니라 단순 sum 으로 계산하면 최악의 경우 O(MxN)
# 누적합 배열을 미리 만들어놓으면 O(1)로 계산 가능

# 누적합 배열(prefix[k]는 처음부터 k-1번째까지의 합)
prefix = [0 for _ in range(N+1)]
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + numbers[i-1]

# 구간합
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])