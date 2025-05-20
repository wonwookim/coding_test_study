# 32412kb	36ms
N = int(input()) 
K = int(input())  
recommend = list(map(int, input().split()))

photo = []  
recommend_count = dict()  
time_stamp = dict()  

for t, student in enumerate(recommend):
    if student in photo:
        # 사진이 있으면 추천수만 증가
        recommend_count[student] += 1
    else:
        if len(photo) < N:
            # 사진에 자리가 있으면 그냥 추가
            photo.append(student)
            recommend_count[student] = 1
            time_stamp[student] = t
        else:
            # 추천 수 가장 적고, 오래된 학생 제거
            # 추천 수 -> 시간 순으로 정렬해서 첫 번째 제거
            photo.sort(key=lambda x: (recommend_count[x], time_stamp[x]))
            remove_student = photo.pop(0)
            del recommend_count[remove_student]
            del time_stamp[remove_student]

            # 새 학생 추가
            photo.append(student)
            recommend_count[student] = 1
            time_stamp[student] = t


print(' '.join(map(str, sorted(photo))))
