# 시간: 268ms, 메모리: 41144KB -> numbers 변수를 지정했을 때
# 시간: 208ms, 메모리: 42168KB -> numbers 변수를 지정하지 않았을 때
# numbers 변수를 지정했을 때가 메모리를 더 차지할 것이라고 생각했는데 아님

# N: 숫자의 개수, M: test case (1 <= M,N <= 100,000)
# N개의 숫자들의 나열
# M번의 test case

# 잘못된 접근 -> 시간 초과
    # 슬라이싱을 이용한 구간 합 구하기

# 접근
    # 미리 각 index까지의 누적 합 구하기 -> 최악: 100,000 (N의 개수만큼) -> 충분히 시간 가능
    # prefix_sum에 담아두기
    # prefix_sum[end] - prefix_sum[start - 1] -> start - 1을 하는 이유는 start index의 값은 더해야 해서

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
# 누적 합 저장하는 변수
prefix_sum_list = [0]
numbers = list(map(int, input().split()))

# 미리 누적 합 저장
for idx, num in enumerate(numbers):
    prefix_sum = prefix_sum_list[idx] + num
    prefix_sum_list.append(prefix_sum)

# start, end에 각각 접근하여 단순 뺄셈으로 문제 해결
for _ in range(M):
    start, end = map(int, input().split())
    print(prefix_sum_list[end] - prefix_sum_list[start - 1])
