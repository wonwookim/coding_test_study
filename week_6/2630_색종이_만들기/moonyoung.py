# 메모리 : 32412 KB, 시간 : 40 ms
import sys
N = int(sys.stdin.readline())

paper = []
blue = 0
white = 0

for _ in range(N) :
  paper_input = map(int, sys.stdin.readline().split())
  paper.append(list(paper_input))

def paper_check(x, y, size) :
  global white, blue
  # 첫 번째 값을 기준으로
  first = paper[x][y]
  for i in range(x, x + size) :
    for j in range(y, y + size) :
      if paper[i][j] != first :
        new_size = size // 2 
        paper_check(x, y, new_size)
        paper_check(x, y + new_size, new_size)
        paper_check(x + new_size, y, new_size)
        paper_check(x + new_size, y + new_size, new_size)
        return
  if first == 0 :
    white += 1
  else :
    blue += 1

paper_check(0, 0, N)

print(white)
print(blue)