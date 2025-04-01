N = int(input())
char_list = []
stack = []
for _ in range(N) :
  char = input()
  char_list.append(char)

for _ in range(len(char_list)) :
  if char_list[i] == 'push' :
    stack.append(X)
  elif char_list[i] == 'pop' :
    if len(stack) == 0 :
      print(-1)
    else : 
      char_list.pop(-1)
  elif char == 'size' :
    print(len(char_list))
