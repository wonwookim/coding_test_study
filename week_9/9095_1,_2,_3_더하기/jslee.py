#메모리 : 32412KB, 시간 : 48ms



T = int(input())

for _ in range(T):
    N = int(input())
    D = [0] * (max(4, N+1))  # 최소 크기 확보 (최소 D[3])

    D[1] = 1
    D[2] = 2
    D[3] = 4
    # D(n) = D(n-1) + D(n-2) + D(n-3)
    for i in range(4, N + 1):
        D[i] = D[i - 1] + D[i - 2] + D[i - 3]

    print(D[N])
