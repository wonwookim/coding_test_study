import sys

N = int(sys.stdin.readline())
nm = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

low = 0 # 최소값
high = M # 최대값 
total = 0
mid = (low + high) // 2
answer = 0



if sum(nm) <= M:
  print(max(nm))
else:
  while low <= high:
    for i in range(len(nm)):
      if nm[i] <= mid:
        total += nm[i]
      else:
        total += mid

    
    if total> M:
      high = mid - 1
      total = 0
    elif total <= M:
      low = mid + 1
      total = 0
      answer = mid
    mid = (low + high) // 2
  print(answer)




