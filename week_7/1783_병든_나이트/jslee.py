N, M = map(int, input().split())
result = 0

if N == 1:
  result = 1

elif N == 2: 
  if 1 <= M <= 6: #m이 1~6일 때
    result = (M + 1) // 2
    
  elif M >= 7: #7이상일 때
    result = 4
    
elif N >= 3: 
  if M <= 6: #m이 1~6일 때
    result = min(M, 4)
  elif M >= 7: #m이 7 이상일 때
    result = M - 2

print(result)
