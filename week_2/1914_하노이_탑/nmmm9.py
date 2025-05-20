
# N개의 원판을 1번 → 3번으로 옮기려면
# N-1개를 1번 → 2번으로 옮기고
# 가장 큰 N번 원판을 1번 → 3번으로 옮기고
# N-1개를 2번 → 3번으로 옮긴다
# 이 과정을 반복


import sys

def hanoi(n, start, mid, end):
    if n == 1:
        # 원판 1개일 때는 바로 이동
        print(f"{start} {end}")
        return

    # 1단계: n-1개를 보조 기둥으로 이동 (start → mid, end 사용)
    hanoi(n - 1, start, end, mid)

    # 2단계: 가장 큰 원판 n번을 목적지로 이동
    print(f"{start} {end}")

    # 3단계: n-1개를 목적지로 이동 (mid → end, start 사용)
    hanoi(n - 1, mid, start, end)

n = int(sys.stdin.readline())

print(2**n - 1)

if n <= 20:
    hanoi(n, 1, 2, 3)  
else:
    print(2**n - 1)


# n=3 일때 함수 호출 과정
#    hanoi(3, 1, 2, 3)
#    ├── hanoi(2, 1, 3, 2)
#    │   ├── hanoi(1, 1, 2, 3)   → print: 1 3
#    │   └── print: 1 2
#    │   └── hanoi(1, 3, 1, 2)   → print: 3 2
#    ├── print: 1 3
#    └── hanoi(2, 2, 1, 3)
#        ├── hanoi(1, 2, 3, 1)   → print: 2 1
#        └── print: 2 3
#        └── hanoi(1, 1, 2, 3)   → print: 1 3
