## 메모리 : 42728 KB, 시간 : 232ms
# 이분 탐색을 사용
# 공유기 사이의 최소 거리를 이분 탐색의 기준으로
import sys
N, C = map(int, sys.stdin.readline().split())
x_list = []
for _ in range(N) :
  x_list.append(int(sys.stdin.readline()))

x_list = sorted(x_list)

left = 1 # 최소길이
right = x_list[-1] - x_list[0] # 최대길이

max_distance = 0

while left <= right :
  mid = (left + right) // 2

  def check_distance(distance) : # 거리로 C를 설치할 수 있는지
    count = 1 
    last_installed = x_list[0]
    
    for x in x_list :
      if x - last_installed >= distance:  # 이전 설치한 집과의 거리가 distance 이상이면 설치 
        count += 1
        last_installed = x # 최근 설치 지점 업데이트

    if count >= C : # 설치 수가 c가 되면 true
      return True
    else :
      return False
    
  if check_distance(mid) : 
    max_distance = mid
    left = mid + 1
  else :
    right = mid - 1

   
print(max_distance)
