# 시간: 448ms, 메모리: 42728KB

# N: 집의 개수, C: 공유기 개수
# 접근
    # 공유기 사이의 거리를 찾는 이분탐색을 사용
        # 공유기 사이의 거리 (1 ~ 가장큰 값 - 가장 작은 값)
        # mid 구하기
        # for 구문 이용
            # 해당 집의 좌표가, mid + 이전 집보다 크면 count -> 우리가 정한 공유기 간의 거리보다 길다는 의미
            # 아니면 x
        # count 값이 C보다 작으면 우리가 설정한 길이가 너무 길다는 것 -> end를 mid - 1로 설정
        # count 값이 C보다 크면 우리가 설정한 길이가 너무 짧다는 것 -> start를 mid + 1로 설정

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house_axis = sorted([int(input()) for _ in range(N)])

start, end = 1, house_axis[-1] - house_axis[0]
answer = 1

while start <= end:
    count = 1
    prev = house_axis[0]
    mid = (start + end) // 2

    for house in house_axis:
        if house >= mid + prev: # 이전 값에 거리를 더한 값보다 house가 더 크면
            count += 1 # 우리가 정한 공유기 간의 거리보다 길기 때문에 count해줌
            prev = house # 이동했다는 것을 확인
    
    if count < C : # 최대 공유기 개수보다 더 작으면 공유기 간 거리를 더 줄여야하기 때문에 end 쪽을 더 줄이기
        end = mid - 1
        
    else:
        start = mid + 1
        answer = max(answer, mid) # answer는 최대 값을 가져야하기 때문에

print(answer)
