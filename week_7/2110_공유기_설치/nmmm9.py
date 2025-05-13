#시간 5300ms  메모리 41164KB
n, c = map(int, input().split())
houses = []

for _ in range(n):
    houses.append(int(input()))

houses.sort()
start = 1  # 공유기 사이 최소 거리는 1 이상
end = houses[-1] - houses[0]  # 가장 먼 거리
result = 0

while start <= end:
    mid = (start + end) // 2  # 현재 공유기 간 최소 거리 후보

    # 첫 번째 집에 무조건 설치
    count = 1
    last = houses[0]  # 마지막으로 공유기 설치한 위치

    # 두 번째 집부터 끝까지 돌면서 공유기 설치
    for i in range(1, n):
        # 현재 집이 마지막 설치 위치보다 거리만큼 떨어져 있으면 설치
        if houses[i] - last >= mid:
            count += 1
            last = houses[i]

    # 공유기를 C개 이상 설치할 수 있는 경우 거리 늘려보기
    if count >= c:
        result = mid         # 가능한 거리니까 저장
        start = mid + 1      # 더 넓게 설치 가능한지 확인
    else:
        end = mid - 1        # 공유기 부족  거리 줄여야 함

print(result)
