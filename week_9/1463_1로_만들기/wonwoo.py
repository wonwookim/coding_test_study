# 시간: 32ms, 메모리: 32412KB

# N: 정수 (1 <= N <= 10^6)

# 접근(dp)
    # array에 각 정수마다의 최소 횟수를 저장
    # n이 3으로 나누어 떨어지면 -1 했을 때 값과, 3으로 한번 나눴을 때 값 중 더 작은 값에 + 1
    # n이 2로 나누어 떨어지면 -1 했을 때 값과 2로 한번 나눴을 때 값 중 더 작은 값에 + 1
    # 나머지 경우는 그냥 -1 했을 때 값에 + 1

    # 2와 3 동시에 나눠지면, 그때는 2 or 3으로 나눴을 때 값의 최소 + 1로 설정해야함 -> 이거 안 하면 시간초과
import sys
N= int(sys.stdin.readline())

array = {1: 0}

def func(num):
    if num in array.keys():
        return array[num]
    if num % 2 == 0 and num % 3 == 0:
        array[num] = min(func(num // 2) + 1, func(num // 3) + 1)
    elif num % 2 == 0:
        array[num] = min(func(num // 2) + 1, func(num -1) + 1)
    elif num % 3 == 0:
        array[num] = min(func(num // 3) + 1, func(num -1) + 1)
    else:
        array[num] = func(num - 1) + 1
    return array[num]

print(func(N))