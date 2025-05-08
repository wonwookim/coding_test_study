# 메모리 : 32412 KB, 시간 : 36ms
N = int(input())
quad = []
for _ in range(N) :
  quad_input = input()
  quad.append(list(quad_input))

def quad_tree(x, y, size) :
  first = quad[x][y]
  for i in range(x, x + size) :
    for j in range(y, y + size) :
      if quad[i][j] != first :
        new_size = size // 2 
        left_up = quad_tree(x, y, new_size)
        right_up = quad_tree(x, y + new_size, new_size)
        left_down = quad_tree(x + new_size, y, new_size)
        right_down = quad_tree(x + new_size, y + new_size, new_size)
        return '(' + left_up + right_up + left_down + right_down + ')'
  return first

print(quad_tree(0,0,N))