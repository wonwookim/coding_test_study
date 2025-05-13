N = 5
C = 3
home = [1,2,4,8,9]
dist = 0
mid = 0

low = 1  # 공유기 사이 최소 거리 (0은 불가)
high = home[-1] - home[0] # 최대 거리
mid = (low + high) // 2
while low <= high:
    mid = (low + high) // 2
    install_count = 1
    last_installed = home[0]
    for i in range(1, N):
        if home[i] - last_installed >= mid:
            install_count += 1
            last_installed = home[i]
    if install_count >= C:
        dist = mid 
        low = mid + 1
    else:
        high = mid - 1

print(dist)
