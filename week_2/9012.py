import sys

input = sys.stdin.readlines()

for i in input[1:]:
    stack = []
    is_break = False
    for j in i.strip(): # 테스트 별로 확인
        if j == ')': # )인 경우
            if len(stack) == 0: # 더이상 제거할 (가 없을 때
                is_break = True
                break # 오류로 빠져나오기
            stack.pop() # break가 안 걸리면 빠져나오기
        if  j == '(': # (인 경우
            stack.append('(') # 추가

    if is_break or len(stack) > 0:  # 위에서 멈추거나, 아직 지워야할 (가 남아있을 경우
        print('NO')
    else:
        print('YES')
    