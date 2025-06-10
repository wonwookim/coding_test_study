#시간 72ms  메모리 43168KB
#1차 시도: 시간초과(리스트 & for문 반복)
#2차 시도: 세트+교집합 이용(중복없음)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seen = set(input().strip() for _ in range(N))
heard = set(input().strip() for _ in range(M))

answer = sorted(seen & heard)

print(len(answer))
for name in answer:
    print(name)

# answer = []
# for i in range(len(seen)):
#     for j in range(len(heard)):
#         if seen[i] == heard[j]:
#             answer.append(seen[i])
#         else:
#             continue
# answer = sorted(answer)

# print(len(answer))
# for i in range(len(answer)):
#     print(answer[i])