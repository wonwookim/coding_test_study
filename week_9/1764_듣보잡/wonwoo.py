# 시간: 96ms, 메모리: 43168KB
# N: 듣도 못한 사람의 수, M: 보도 못한 사람의 수

# 접근:
#     1. 듣도 못한 사람과 보도 못한 사람의 이름을 각각 입력받아 set으로 저장
#     2. 두 set의 교집합을 구하여 듣도 못한 사람 중 보도 못한 사람의 이름을 찾기


import sys

input = sys.stdin.readline
N, M = map(int, input().split())

not_heard = set()
for _ in range(N):
    not_heard.add(input().strip())

not_seen = set()
for _ in range(M):
    not_seen.add(input().strip())

# 교집합을 구하여 듣도 못한 사람 중 보도 못한 사람의 이름을 찾기
result = sorted(not_heard & not_seen)

print(len(result))
for name in result:
    print(name)