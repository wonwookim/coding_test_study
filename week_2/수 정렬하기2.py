# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

N = int(input()) # 수의 개수수

x_list = []
for i in range(N) :
  x = int(input())
  x_list.append(x)
x_list.sort() # 오름차순 정렬렬

for i in range(len(x_list)) :
  print(x_list[i])