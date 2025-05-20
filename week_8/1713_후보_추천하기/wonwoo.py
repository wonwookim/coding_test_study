# 첫번쨰 줄: 선거 후보의 수 N
# 두번쨰 줄: 학생들이 찍은 후보의 수 M
# 세번쨰 줄: 학생들이 찍은 후보의 번호들
# 접근
    # heapq를 사용하여 count가 적은 순으로 나열 -> x
    
    # votes_list를 for
        # votes의 key에 해당하는 후보가 있는 경우 +1
        # 없을 경우 만약 frame의 길이가 3보다 크면 조건에 해당 되는 애 제거
        # votes와 time의 dict에서도 해당 key 제거
        # 그리고 새로운 person을 frame, votes, time에 추가
import sys
input = sys.stdin.readline
N = int(input())  # 사진틀 개수
M = int(input())  # 추천 횟수
vote_list = list(map(int, input().split()))  # 추천받은 후보 목록

frame = []      # 사진틀에 게시된 후보자 번호
votes = {}      # 후보자 번호 : 추천 수
time = {}       # 후보자 번호 : 게시된 시간

for t, person in enumerate(vote_list):
    if person in votes:
        votes[person] += 1
    else:
        if len(frame) >= N:
            # 내림차순 정렬: 추천 수 적고, 오래된 후보가 뒤로 감
            frame.sort(key=lambda x: (votes[x], time[x]), reverse= True)
            removed = frame.pop()  # 가장 뒤에 있는 후보 제거
            del votes[removed]
            del time[removed]
        frame.append(person)
        votes[person] = 1
        time[person] = t

# 최종 출력: 후보자 번호 오름차순
print(' '.join(map(str, sorted(frame))))
