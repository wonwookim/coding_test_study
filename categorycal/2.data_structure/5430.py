import sys
from collections import deque
N = int(sys.stdin.readline().strip())
for _ in range(N):
    numbers = []
    c = sys.stdin.readline().strip() # 명령
    n = sys.stdin.readline().strip() # 단어수
    numbers = sys.stdin.readline().strip() # 숫자 [1,2,3,4]
    if numbers == "[]":
        numbers = deque()  # 빈 deque
    else:
        numbers = deque(map(int, numbers[1:-1].split(',')))
    for i in range(len(c)):
        if c[i] == 'R':
            numbers.reverse()
        elif c[i] == 'D':
            if numbers:
                numbers.popleft()
            else:
                print('error')
                break
    numbers = list(numbers)
    print(numbers)