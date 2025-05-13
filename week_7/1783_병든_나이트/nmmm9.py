#시간 40ms  메모리 32412KB

n, m = map(int, input().split())

# 세로 1칸이면 이동 불가 → 시작 칸만 방문
if n == 1:
    print(1)

# 세로 2칸이면 위로 두 칸 이동 불가 → 최대 4칸까지 가능
elif n == 2:
    print(min(4, (m + 1) // 2))

# 세로 3칸 이상
else:
    # 가로 7칸 미만이면 최대 4칸까지만 이동 가능
    if m < 7:
        print(min(4, m))
    # 가로 7칸 이상이면 이동 제약 없음 → M - 2칸 방문 가능
    else:
        print(m - 2)
