## 메모리 : 41144 KB, 시간 : 216 ms

# 누적합으로 안 풀고 그냥 슬라이싱 했다가 당연하게도 바로 시간초과 당했습니다... 
import sys
N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

sum = [0]
for num in N_list :
  sum.append(sum[-1] + num) # 마지막 요소에 숫자를 더해서 누적합을 만들기
  # 첫 번째 값에 0 넣지 않으면 빈값이라 인덱스 오류남 
for _ in range(M) :
  i, j = map(int, sys.stdin.readline().split())
  print(sum[j] - sum[i-1])