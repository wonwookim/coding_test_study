## 메모리 : 32544 KB, 시간 : 40ms

# N이 1일 때는 위아래로 움직일 수 없으므로 최대가 1
# N이 2일 때는 위아래로 1칸씩만 이동 가능
# 이 때 오른쪽으로는 2칸씩 이동하기 때문에 (M+1)//2번 이동 가능
# 그러나 4번이 한계이므로 min(4, (M + 1) // 2)
# N이 3이상 M이 7이하일 때도 4번이 한계이므로 min(4, M)
# N, M둘 다 클 때는 제한이 사라짐

import sys

N, M = map(int,sys.stdin.readline().split())

if N == 1 :
    max_visit = 1
elif N == 2 :
    max_visit = min(4, (M + 1) // 2)
elif N >= 3 and M < 7 :
    max_visit = min(4, M)
elif N >= 3 and M >= 7 :
    max_visit = M - 2

print(max_visit)