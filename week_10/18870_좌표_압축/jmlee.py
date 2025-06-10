#시간 1352ms, 메모리 186212KB
import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int,input().split()))
sorted_nums = sorted(set(nums))

# 접근3: dict로 매핑
# 중복 제거하고 오름차순 정렬 -> 각 숫자에 번호 매겨서 출력
dict_num = {n:idx for idx, n in enumerate(sorted_nums)}

result = ' '.join(str(dict_num[n]) for n in nums)
print(result)

# 접근2: 이진탐색으로 풀어보자
# 시간 7656ms ..?
# for n in nums:
#     left = 0
#     right = len(sorted_nums) -1
#     while left <= right:
#         mid = (left + right) // 2
#         if sorted_nums[mid] < n:
#             left = mid + 1
#         else:
#             right = mid - 1
#     print(left, end= ' ')

# 접근1: 자꾸 완전탐색으로 풀게 된다.. 역시 시간초과
# 그래도 완전탐색으로 로직 먼저 이해하기는 쉬움
# for i in range(N):
#     result = set() # result를 매번 초기화시켜줘야한다
#     for j in range(N):
#         if nums[i] > nums[j]:
#             result.add(nums[j])
#     print(len(result), end=' ')
