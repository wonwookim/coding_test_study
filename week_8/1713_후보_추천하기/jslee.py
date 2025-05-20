N = int(input())
S = int(input())
listset = list(map(int, input().split()))

frame = []
dict33 = {}

for i in range(S):
    student = listset[i]

    # 이미 사진틀에 있는 경우 → 추천 수 증가만
    if any(s == student for _, s in frame):
        dict33[student] += 1

    # 아직 사진틀에 없는 경우
    elif len(frame) < N:
        dict33[student] = 1
        frame.append((i, student))

    else:
        # 제거 대상 선정
        playlist = []
        for time, s in frame:
            playlist.append((dict33[s], time, s))

        playlist.sort()
        to_remove = playlist[0][2]

        # 추천 dict, frame에서 제거
        dict33.pop(to_remove)
        frame = [t for t in frame if t[1] != to_remove]

        # 새 학생 등록
        dict33[student] = 1
        frame.append((i, student))

# 학생 번호만 꺼내서 정렬 후 출력
answer = sorted(s for _, s in frame)
print(*answer)
