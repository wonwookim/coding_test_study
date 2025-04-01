# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

import math
n = int(input()) # 수의 개수 N
nums = list(map(int, input().split())) # N개의 수 입력력
prime_list = []

def prime(x): # 소수인지 판별하는 함수
  if x < 2:
      return False # 2보다 작으면 X
  # 2부터 자신의 제곱근까지 반복하면서 나누어떨어진다면 
  # 소수가 아닌 것임 ( 공식은 검색했습니다 . . )
  for i in range(2, int(math.sqrt(x)) + 1):
      if x % i == 0:
          return False
  return True


for i in range(n) :
  if prime(nums[i]):
    prime_list.append(nums[i])
print(len(prime_list))