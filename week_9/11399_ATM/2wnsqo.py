# 32412KB	36ms
import sys
N = int(sys.stdin.readline().strip())
time = list(map(int, sys.stdin.readline().strip().split()))

time.sort()
t = 0
result = 0
for i in range(len(time)):
    t += time[i] # 앞 사람 걸린시간 + 자기 걸린 시간
    result += t # 누적 시간 

print(result)