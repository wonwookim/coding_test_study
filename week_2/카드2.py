from collections import deque
N = int(input())
dq= deque([])
# 여기서 집합 쓸 수 없는 이유 : 
# 집합은 pop이 안 됨
# 되긴 하는데 무작위로 pop해서
# 첫 번째 값 pop 불가능

for i in range(1, N+1) :
  dq.append(i)

while len(dq) >= 2 :
  dq.popleft()

  X = dq.popleft()
  dq.append(X)

print(dq[0])