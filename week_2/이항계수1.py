import math

N, K = map(int, input().split())

result = int(math.factorial(N) / (math.factorial(N-K) * math.factorial(K)))

print(result)
