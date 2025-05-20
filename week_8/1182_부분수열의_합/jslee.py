N, S = map(int, input().split())
listset = list(map(int, input().split()))
    
count = 0
for mask in range(1, 1 << N):
    value = 0
    for i in range(N):
        if mask & (1 << i):
            value += listset[i]

    if value == S:
        count+=1


print(count)
