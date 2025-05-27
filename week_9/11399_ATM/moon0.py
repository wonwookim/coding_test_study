## 메모리 : 32544KB, 시간 : 48ms

# 인출 시간이 짧은 사람이 앞에 있을 수록 다음 사람들이 적게 기다리기 때문에
# 오름차순으로 정렬해두면 무조건 최소가 나옴

import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P = sorted(P) # 짧게 걸리는 사람이 먼저 와야 뒤에 오는 사람들의 대기시간이 줄어듦

total_time = 0
acc_time = 0  # 누적된 시간

for time in P :
    acc_time += time
    total_time += acc_time
    print(acc_time)
    print(total_time)

print(total_time)
