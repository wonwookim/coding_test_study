#메모리 : 32412KB, 시간 : 36ms

N = int(input())
heap_fail = []
heap_fail= list(map(int, input().split()))


total = 0
acc = 0 

heap_fail.sort()

for ti in heap_fail:
    acc += ti
    total += acc


print(total)
