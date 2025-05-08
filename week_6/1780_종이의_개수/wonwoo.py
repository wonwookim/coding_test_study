# 시간 : 4084ms, 메모리 : 79592KB
# N : 종이의 크기 (N X N)
# 접근 :
    # 재귀함수 이용
    # for 구문을 돌면서 다른 값을 갖는지 확인 
        # 다른 값이 존재하지 않으면 해당 값에 count + 1
        # 1개라도 다르면 for 구문 멈추고 9개의 지역으로 분할 후 위 작업 진행
import sys

input = sys.stdin.readline
N = int(input())

array = [ list(map(int,input().strip().split())) for _ in range(N)] # 전체 종이
answer = {i : 0 for i in range(-1, 2)} # -1, 0, 1의 개수 count하기 위한 변수


def cut_paper(array):
    is_same = True
    key = array[0][0]
    for row in array:        
        for char in row:
            if key != char: # 1개라도 다른 경우 찾기
                is_same = False
                break
        if not is_same: # 1개라도 다르면 더 찾아볼 필요 없음
            break

    if is_same: # 모든 요소가 같은 경우 멈추기
        answer[key] += 1 
        return
    
    # 한개라도 다를 경우 분할하기
    batch_size = len(array) // 3
    for i in range(0, 3):
        for j in range(0, 3):
            batch_array = [ row[j * batch_size : (j + 1) * batch_size] for row in array[i * batch_size : (i + 1) * batch_size]]
            cut_paper(batch_array)
    return 

cut_paper(array)


for i in answer: # 이렇게 했을 때, 계속 틀렸다고 했음 -> dict에서 무슨 순서를 보장 못 하나봄
  print(answer[i]) 
# for i in [-1, 0, 1]:
#     print(answer[i])