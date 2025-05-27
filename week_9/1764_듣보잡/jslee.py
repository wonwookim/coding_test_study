#메모리 : 45064KB, 시간 : 2448ms



not_seen = []
not_listen = []

non_human = []


N, M = map(int, input().split())
for i in range(N):
    not_seen.append(input())

for i in range(M):
    not_listen.append(input())


non_human = sorted(list(set(not_seen) & set(not_listen)))
print(len(non_human))
for non in non_human:
    print(non)
