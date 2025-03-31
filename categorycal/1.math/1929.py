# 	34536kb 5812ms
import sys
import math
a, b = map(int,sys.stdin.readline().split())
if a == 1:
    a +=1
for i in range(a,b+1):
    c = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i % j ==0:
            c += 1
            break
    if c == 0:
        print(i)