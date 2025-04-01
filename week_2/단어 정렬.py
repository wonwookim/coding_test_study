# 알파벳 소문자로 이루어진 N개의 단어가 들어오면
# 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

N = int(input())  # 단어의 개수 N
char_list = [] # 단어 리스트에 담기기
for _ in range(N):
    char = input() # 단어는 입력받음음
    if char not in char_list:
        char_list.append(char)  # 중복되지 않는다면 리스트에 추가가

char_list.sort(key=lambda x: (len(x), x)) # 정렬 1. 길이 , 2. 사전순

for i in range(len(char_list)) :
  print(char_list[i])