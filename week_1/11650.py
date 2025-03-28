import sys
input = sys.stdin.readlines
cors = input()[1:]
cors.sort(key = lambda cor: (int(cor.strip().split()[0]), int(cor.strip().split()[1])) )
print(''.join(cors)) # 글자 뒤에 \n이 숨겨져 있어서 자동으로 줄 바꿈이 됨