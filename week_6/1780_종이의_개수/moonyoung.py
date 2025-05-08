# 메모리 : 71308 KB, 시간 : 3584 ms
import sys
N = int(sys.stdin.readline())

paper = []
count = [0,0,0]
for _ in range(N) :
  paper_input = map(int, input().split())
  paper.append(list(paper_input))

def paper_check(x, y, size) :
  # 첫 번째 값을 기준으로
   first = paper[x][y]
   for i in range(x, x + size) :
    for j in range(y, y + size) :
      if paper[i][j] != first :
        new_size = size // 3 # size를 3으로 나누는 이유 => 항상 3의 거듭제곱이라서
        for dx in range(3) : 
          for dy in range(3) :
            new_x = x + dx * new_size
            new_y = y + dy * new_size
            paper_check(new_x, new_y, new_size)
        return
   count[first + 1] += 1

paper_check(0, 0, N)
for c in count :
  print(c)  