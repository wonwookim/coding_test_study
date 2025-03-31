# 	37528kb 144ms
import sys
from itertools import permutations
a, b = map(int,sys.stdin.readline().split())

num = []
for i in range(1,a+1):
    num.append(i)

result = list(permutations(num, b))  # 2개씩 뽑아 조합 생성

# 언패킹킹
for r in result:
    print(*r)
