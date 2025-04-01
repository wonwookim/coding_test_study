# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

N = int(input()) 
A = set(map(int, input().split())) # n개의 정수
# 리스트가 아닌 이유 : 시간초과 ^^

M = int(input())
B = list(map(int, input().split()))

result = []

for i in range(M) :
  if B[i] in A : # 리스트 b가 a에 있다면면
    result.append(1) 
  else :
    result.append(0)

for i in result :
  print(i)