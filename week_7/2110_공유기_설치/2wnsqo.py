# 41164KB	724ms
import sys

# N : 집의 개수  C : 공유기 개수
N, C = map(int, sys.stdin.readline().strip().split(' '))

house = []
for _ in range(N):
    house.append(int(sys.stdin.readline().strip()))

house.sort() # 좌표 정렬
start = 1 # 공유기 거리 사이 최소값
end = house[-1] - house[0] # 공유기 사이 거리 최대값 
result = 0

while start <= end:
    mid = (start+end)//2 # 기준(공유기를 몇 칸씩 띄어 설치 할건지 )
    count = 1 # 첫번째 집에 설치
    index = 0 # 마지막 설치한 집 인덱스스
    for i in range(1, N): # 다음 집 찾기기
        if house[i] >= house[index] + mid:
            index = i
            count +=1

    if count >= C: # 많이 설치 가능
        result = mid  # 이 거리로도 설치 가능하니까 저장 -- 가능한 걸 저장
        start = mid + 1  # 더 넓게 벌릴 수 있는지 시도
    else:
        end = mid - 1  # 설치 개수가 부족하면 거리 줄여야 함


print(result)