N = int(input())
t_shirts = list(map(int, input().split()))
T, P = map(int, input().split())
t_result = 0

for i in range(6) :
  t_result += (t_shirts[i] // T) + 1
  if t_shirts[i] % T == 0 :
    t_result -= 1
p_1 = N // P
p_2 = N % P
    
print(t_result)
print(p_1, p_2)