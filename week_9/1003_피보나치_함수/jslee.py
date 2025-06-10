#메모리 : 32412KB, 시간 : 56ms

T = int(input())
max_n = 40 # 최대 범위
count_0 = [0] * (max_n + 1)
count_1 = [0] * (max_n + 1)

# 초기 조건
count_0[0] = 1
count_1[0] = 0
count_0[1] = 0
count_1[1] = 1

# 바텀업
for i in range(2, max_n + 1):
    count_0[i] = count_0[i - 1] + count_0[i - 2]
    count_1[i] = count_1[i - 1] + count_1[i - 2]


for _ in range(T):
    n = int(input())
    print(count_0[n], count_1[n])
