import math

a, b = map(int, input().split())

max_x = math.gcd(a,b)

min_x = a * b // max_x

print(max_x)
print(min_x)