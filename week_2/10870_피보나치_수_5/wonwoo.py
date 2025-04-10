# 시간: 36ms, 메모리: 32412KB
# 시간: 36ms, 메모리: 32412KB 동일
# [0, 1] 기본 값
# fn = fn-2 + fn-1
# f1 = 0 + 1
# f2 = 1 + f1
# f3 = f1 + f2
import sys

input = sys.stdin.readline
fibonacci_list = []
num = int(input())

# def fibonacci_numbers(num, i):
#     if num < i:
#         return fibonacci_list[-1]
#     fibonacci_list.append(i if i < 2 else fibonacci_list[i-2] + fibonacci_list[i-1])
#     i += 1
#     return fibonacci_numbers(num, i)

# print(fibonacci_numbers(num, 0))

def fibonacci_numbers(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci_numbers(num-1) + fibonacci_numbers(num-2)

print(fibonacci_numbers(num))