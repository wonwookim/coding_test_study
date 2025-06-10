# 32412kb	40ms

n = int(input())
time = list(map(int, input().split()))
time.sort()

total = 0
acc = 0
for t in time:
    acc += t
    total += acc

print(total)
