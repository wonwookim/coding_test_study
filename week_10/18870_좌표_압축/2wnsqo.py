# 172328KB	1856ms
import sys

N = int(sys.stdin.readline().strip()) # 숫자의 개수
nums = list(map(int, sys.stdin.readline().strip().split()))
set_nums = set(nums)
sorted_nums = sorted(set_nums)
dic = {}

for idx,num in enumerate(sorted_nums):
    dic[num] = idx

for i in nums:
    print(dic[i], end=' ')


