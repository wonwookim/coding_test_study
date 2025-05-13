#시간 40ms 메모리 33432KB
import sys
input = sys.stdin.readline

N = int(input())
#적은 순서대로 정렬(이진탐색 전제조건)
city = sorted(list(map(int, input().split())))
budget = int(input())

#이진탐색+그리디로 풀기
def is_valid(mid):
    total = 0
    for c in city:
        if c > mid:
            total += mid
        else:
            total += c
    return total <= budget

#이진탐색 초기 범위
#처음엔 mid 초기값을 전체예산//N 이라 생각했는데, 이건 단순평균이고
#문제에서 중요한 건 각 도시가 요청한 예산 중 어떤 상한선(mid)을 정했을 때 전체 예산을 넘는지 판단해야함
#그래서 초기 상한액(mid)는 요청값 범위 내 중간값이 된다

#초기 low가 요청의 최솟값이 아니라 0인 이유는
#상한액은 요청 금액 중 일부를 잘라낼 때의 기준선이고, 반드시 요청금액 중 하나일 필요가 없다
#예시: 요청이 [100, 200, 300]이고 총예산이 200이라면, 상한액은 66일 수도 있다
#그러면 모든 도시에 66씩 배정해서 총 198. 이처럼 상한액은 요청된 값보다 작을 수 있고, 심지어 0도 가능해야 한다.
#반대로, 요청예산이 큰데 총예산이 아예 0일수도 있기 때문에 low는 0이어야한다.
low = 0
high = max(city) #최대 요청값보다 큰 값을 줄 필요 없음
result = 0 #정답(최대 상한액)

#이진탐색 수행
while low <= high:
    mid = (low + high) // 2
    if is_valid(mid):
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)


