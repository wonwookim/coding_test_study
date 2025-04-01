#  첫째줄 : 상근이가 가지고 있는 숫자 카드 개수
#  둘째줄 : 숫자 카드에 적혀있는 정수
#  셋째줄 : m
#  넷째줄 : 몇개있는지 세어야하는수
from collections import Counter

N = int(input())
X = list(map(int, input().split()))

M = int(input())
Y = list(map(int, input().split()))

counter = Counter(X)

for y in Y :
  print(counter[y], end=' ')
