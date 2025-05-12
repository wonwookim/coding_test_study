#시간:108ms 메모리:38340KB

import sys
import heapq

input_ = sys.stdin.readline
N = int(input_())
heap_min = []
for _ in range(N):
    num = int(input_())
    if heap_min and num == 0:
        print(heapq.heappop(heap_min))
    elif not heap_min and num == 0:
        print(0)
    else:
        heapq.heappush(heap_min, num)
