## 메모리 : 44192KB, 시간 : 80ms
import sys
N, M = map(int, sys.stdin.readline().split())
non_see = set()
non_hear = set()
non_seehear = set()

for _ in range(N) :
  non_see.add(sys.stdin.readline().strip())

for _ in range(M) :
  non_hear.add(sys.stdin.readline().strip())

non_seehear = sorted(non_see & non_hear)

print(len(non_seehear))

for name in non_seehear :
  print(name)