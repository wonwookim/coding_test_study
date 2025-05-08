#메모리: 71232kb 시간: 3656ms

import sys
input = sys.stdin.readline  

n = int(input())  # 종이 크기 입력
paper = [list(map(int, input().split())) for _ in range(n)]  # 종이 상태 2차원 리스트로 입력

# 결과 저장용 리스트
result = [0, 0, 0]

def is_same(x, y, size):
    base = paper[x][y]  # 기준값 (첫 번째 칸)
    for i in range(x, x + size):
        row = paper[i]  # 행 단위로 꺼냄
        for j in range(y, y + size):
            if row[j] != base:  # 하나라도 다르면
                return False  # 같은 종이가 아님ㅇ
    return True  # 전부 같으면 True

# 분할 정복 함수
def divide(x, y, size):
    if is_same(x, y, size):  # 현재 영역이 같은 숫자로만 되어 있으면
        result[paper[x][y] + 1] += 1  # -1 → 0번, 0 → 1번, 1 → 2번 인덱스 증가
        return

    size //= 3  # 9등분을 위해 사이즈를 1/3로 줄임
    for dx in range(3):  # 가로 3등분
        for dy in range(3):  # 세로 3등분
            # 각각의 9개 영역에 대해 재귀 호출
            divide(x + dx * size, y + dy * size, size)

# 처음 전체 종이 영역부터 시작
divide(0, 0, n)

# 결과 출력
print(result[0])  # -1로 이루어진 종이 개수 출력
print(result[1])  # 0으로 이루어진 종이 개수 출력
print(result[2])  # 1로 이루어진 종이 개수 출력