# 159304	1724
n = int(input())
nums = list(map(int, input().split()))

# 중복 제거 + 정렬
sorted_unique = sorted(set(nums))

# 압축값 매핑: 값 → 인덱스
coord = {num: i for i, num in enumerate(sorted_unique)}

# 원래 수를 압축값으로 변환
print(*[coord[x] for x in nums])
