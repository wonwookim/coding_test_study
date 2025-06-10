# 43564kb	788ms
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split()) # n 세로의 크기 m 가로의 크기

map_list = []

for i in range(n):
   nums = list(map(int, sys.stdin.readline().strip().split()))
   if nums.count(2) >=1:
      idx = (i,nums.index(2))
   map_list.append(nums)

visited = [[False] *(m) for _ in range(n)]
result = [[-1] *(m) for _ in range(n)]

que = deque()
visited[idx[0]][idx[1]] = True
que.append((idx,0)) # ((0, 0), 0)]
result[idx[0]][idx[1]] = 0

direc = [(0,1),(1,0),(0,-1),(-1,0)]
while que:
   q = que.popleft()
   idx = q[0]
   c = q[1]

   for d in direc:
      new_idx = (idx[0]+d[0],idx[1]+d[1])
      if ((0<= new_idx[0] < n) and  # <=n 이면 out of index가 난다다
          (0<= new_idx[1] < m)):
         if ((visited[new_idx[0]][new_idx[1]] != True) and 
            (map_list[new_idx[0]][new_idx[1]] ==1)):
         
            visited[new_idx[0]][new_idx[1]] = True
            que.append((new_idx,c+1))
            result[new_idx[0]][new_idx[1]] = c+1

         # elif ((visited[new_idx[0]][new_idx[1]] != True) and 
         #    (map_list[new_idx[0]][new_idx[1]] ==0)):
         #    visited[new_idx[0]][new_idx[1]] = True
         #    result[new_idx[0]][new_idx[1]] = 0
   
for i in range(len(result)):
   for j in range(len(result[i])):
      if map_list[i][j] != 0:
         print(result[i][j],end=" ")
      else:
         print(0,end=" ")
   print()