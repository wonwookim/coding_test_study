# 32412KB	6492ms
import sys
M = int(sys.stdin.readline().strip()) # 수행해야하는 연산 수 
dic = {}
for _ in range(M):
    order = sys.stdin.readline().strip()
    if order[:3] == 'all':
        dic = {}
        for i in range(1,21):
            dic[i] = 1
    elif order[:3] == 'emp':
        dic = {}
    else:
        od, num = order.split()
        num = int(num)
        if od == 'add': # 추가
            dic[num] = 1 
        elif od == 'remove': # 삭제
            if dic.get(num):
                del dic[num]
        elif od == 'check': # 체크
            if dic.get(num):
                print(1)
            else:
                print(0)
        elif od == 'toggle': # 반대 
            if dic.get(num):
                del dic[num]
            else:
                dic[num] = 1
