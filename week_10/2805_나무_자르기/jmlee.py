#시간 2620ms, 메모리 148224KB
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 이진탐색의 전제조건
trees = sorted(list(map(int,(input().split()))))

# 접근법: 이진탐색 + 그리디 (상한액 문제와 비슷하다고 느낌)
# 절단기의 높이를 h라고 할 때, 나무의 최소 길이 M을 갖는 h의 최댓값
def cutTree(h):
    cut = []
    for t in trees:
        # 나무의 길이가 절단선보다 클 때, 잘린 부위 넣기
        if t > h:
            cut.append(t-h)
        # 나무의 길이가 더 짧으면 0
        else:
            cut.append(0)
    # 필요한 나무의 길이 M 이상일 때만 출력
    return sum(cut) >= M

# 이진탐색 초기 범위
low = 0
high = max(trees) # 절단선의 길이가 tree의 최대값보다 크면, 전부 0이 됨
result = 0 # 정답(절단기 높이의 최댓값)

# 이진탐색 수행
while low <= high:
    mid = (low + high) // 2
    if cutTree(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)