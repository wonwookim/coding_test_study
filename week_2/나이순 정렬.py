
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
# 이때, 회원들을 나이가 증가하는 순으로,
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

N = int(input())  # 온라인 저지 회원 수 N
members = []  # 회원 리스트트

for _ in range(N) :
  age, name = input().split()  # 나이 이름 공백으로 구분분
  members.append((int(age), name))

members.sort(key = lambda x : x[0]) # 나이순 정렬

for age, name in members:
    print(age, name)