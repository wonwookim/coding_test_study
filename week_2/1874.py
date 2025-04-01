import sys
# 536ms, 40268KB
# 96ms, 42700KB
num = 1
top_num = None
stack = [] # 원본
answer = []
input = sys.stdin.readlines
nums = input()[1:]
nums = list(map(int,nums))

for i in nums:
    # stack 채우기
    while num <= i:
        stack.append(num)
        answer.append('+')
        top_num = i
        num += 1
    
    top_num = stack.pop()
    if top_num != i :
        print('NO')
        break
    answer.append('-')
        
else:
    print('\n'.join(answer))

# answer = ''
# input = sys.stdin.readlines

# nums = input()[1:]
# nums = list(map(int,nums))

# for i in nums:
#     if num < i:
#         stack += list(range(num+1, i))
#         answer += '+' * (int(i)-int(num))
#         answer += '-'
#         num = i
#     else :
#         answer += '-'
#         temp = stack.pop()
#         if temp != i :
#             print("NO")
#             break

# else :
#     print('\n'.join(list(answer)))