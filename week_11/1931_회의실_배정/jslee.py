# 메모리: 54216KB 시간: 252ms


import sys

n = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 2. 회의 끝나는 시간 기준으로 정렬 (끝 시간이 같으면 시작 시간 기준)
meetings.sort(key=lambda x: (x[1], x[0]))

# 3. 그리디 회의 선택
count = 0
last_end_time = 0

for start, end in meetings:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)
