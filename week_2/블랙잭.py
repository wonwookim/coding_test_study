n, m = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

for i in range(n) :
  while num_sum < m :
    num_sum = max(num[i] + num[i+1] + num[i+2])