import sys
import heapq

input_ = sys.stdin.readline
N = int(input_())
num_list = [int(input_().strip()) for _ in range(N)]

# 힙정렬
# 35508	44
def heap_sort(num_list):
    sort_heap = []
    for i in range(N):
        heapq.heappush(sort_heap, num_list[i])
    for _ in range(N):
        print(heapq.heappop(sort_heap))

# 버블정렬(인접한 두 수의 크기비교)
# 32412	172
def bubble_sort(num_list):
    for i in range(N):
        for j in range(N-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    for i in range(N):
        print(num_list[i])

# 선택정렬(맨앞 요소부터 시작 최소값을 찾아서 교환)
# 32412	100
def selection_sort(num_list):
    for i in range(N):
        min_idx = i
        for j in range(i, N):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

    for i in range(N):
        print(num_list[i])

# 삽입정렬(두번째 원소를 시작으로 앞에 있는 요소가 기준보다 크면 한칸식 밀고 삽입함)
# 32412	156
def insertion_sort(num_list):
    for i in range(1, N):
        key = num_list[i]
        j = i-1
        while j>=0 and key < num_list[j]:
            num_list[j+1] = num_list[j]
            j -= 1
        num_list[j+1] = key

    for i in range(N):
        print(num_list[i])

# **********************************************
# 퀵정렬(기준을 정해서 왼쪽 오른쪽 나눠 재귀적으로 정렬)
# 32412	60
def quick_sort(num_list, low, high):
    if low >= high:
        return
    mid = (low + high)//2
    pivot_candidate = [num_list[low], num_list[mid], num_list[high]]
    pivot = sorted(pivot_candidate)[1]

    left = low
    right = high

    while left <= right:
        while num_list[left] < pivot:
            left += 1
        while num_list[right] > pivot:
            right -= 1
        if left <= right:
            num_list[left], num_list[right] = num_list[right], num_list[left]
            left += 1
            right -= 1

    quick_sort(num_list, low, right)
    quick_sort(num_list, left, high)

quick_sort(num_list, 0, N-1)
for i in num_list:
    print(i)

# 병합정렬 32412	36
# https://wjunsea.tistory.com/132
# https://discord.com/channels/@me/1349987762803179550
def merge_sort(num_list):
    # 배열의 길이가 1 이하면 이미 정렬되었다 가정
    if 1 >= len(num_list):
        return num_list

    # 중간값을 정해 배열을 둘로 나누기
    mid =  len(num_list) // 2
    left_list = num_list[:mid]
    right_list = num_list[mid:]

    # 왼쪽 부분, 오른쪽 부분 재귀적으로 배열 정렬
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    # 병합리스트 & idx 설정
    merge_list = []
    left_idx, right_idx = 0, 0

    # 두 배열을 비교해서 새로운 리스트에 정렬하기
    while left_idx < len(left_list) and right_idx < len(right_list):
        if left_list[left_idx] <= right_list[right_idx]:
            merge_list.append(left_list[left_idx])
            left_idx += 1

        else :
            merge_list.append(right_list[right_idx])
            right_idx += 1

    # 남은 요소 리스트에 담기
    merge_list.extend(left_list[left_idx:])
    merge_list.extend(right_list[right_idx:])

    return merge_list

merge_list = merge_sort(num_list)
for i in merge_list:
    print(i)

# 계수정렬
# https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html
# 계수를 이용하여 정렬
max_val = max(num_list) + 1
count_list = [0] * max_val
def counting_sort(num_list):
    for n in num_list:
        count_list[n] += 1

    sorted_list = []
    for i, cnt in enumerate(count_list):
        sorted_list.extend([i] * cnt)

    return sorted_list

sorted_list = counting_sort(num_list)
for n in sorted_list:
    print(n)



# 기수정렬
def radix_sort(num_list):
    pass

# 버킷정렬
def bucket_sort(num_list):
    pass

# 셸정렬
def shell_sort(num_list):
    pass

# 이진 삽입 정렬
def binary_insertion_sort(num_list):
    pass

# 파이썬 기본 정렬
# 32412	48
num_list.sort()
for i in range(N):
    print(i)