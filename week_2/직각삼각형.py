while True:
  num = list(map(int,input().split()))

  if num == [0, 0, 0] :
    break
  
  num.sort()
  a = num[0]
  b = num[1]
  c = num[2]

  if c*c == (a*a + b*b) :
    print('right')
  else :
    print('wrong')