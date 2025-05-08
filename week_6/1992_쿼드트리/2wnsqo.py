#32412KB	36ms
import sys
N = int(sys.stdin.readline().strip())
listt = []

for _ in range(N):
    a = sys.stdin.readline().strip() # 입력 받기기
    listt.append(a) # 리스트로 합치기 

# print(listt)

def paper(listt):
    answer = listt[0][0]
    same = True
    # 코드는 간결하지만 전체를 다 둘러보기 때문에 시간은 늘어난다
    # same = all(listt[i][j] == answer for i in range(len(listt)) for j in range(len(listt)))
    for i in range(len(listt)):
        for j in range(len(listt)):
            if listt[i][j] != answer:
                same = False
                break
        if same == False:
            break

    if same == True:
        return answer
    else:
        n = int(len(listt) / 2)
        listt2 = []
        result = ''
        for i in range(2):
            for j in range(2):
                # listt2 = listt[i*n:(i+1)*n][j*n:(j+1)*n] # 행으로만 두번 슬라이싱 하게 된다다
                listt2 = ([row[j*n:(j+1)*n] for row in listt[i*n:(i+1)*n]])
                result += paper(listt2) # 결과를 계속 result에 누적적
        return f'({result})' # 괄호를 씌워 출력력
    
print(paper(listt))

# import sys
# N = int(sys.stdin.readline().strip())  # 첫 번째 줄에서 정수 N을 입력받음 (정사각형 한 변의 길이)

# listt = []
# for _ in range(N):
#     a = sys.stdin.readline().strip()       # 각 줄을 문자열로 입력받음 (ex: "11110000")
#     listt.append(a)                         # 문자열 그대로 리스트에 저장 (리스트의 요소가 문자열이 됨)

# def paper(arr):
#     n = len(arr)                            # 현재 배열(서브배열)의 한 변의 길이
#     first = arr[0][0]                       # 첫 번째 문자를 기준으로 전체가 같은 문자인지 판단할 기준값 설정
    
#     # 전체가 같은 수인지 확인 (2중 루프를 한 줄로 처리)
#     same = all(arr[i][j] == first for i in range(n) for j in range(n))
#     if same:
#         return str(first)                   # 모두 같은 수이면 그 숫자 하나만 문자열로 반환
    
#     # 다르면 배열을 4개의 부분으로 나눠서 재귀 호출
#     half = n // 2                           # 반으로 쪼갤 크기
#     result = "("                            # 결과 문자열을 여는 괄호로 시작

#     for i in range(2):                      # 0, 1 — 행 방향 절반으로 나누기
#         for j in range(2):                  # 0, 1 — 열 방향 절반으로 나누기
#             # 부분 배열 만들기: 행 i*half ~ (i+1)*half, 열 j*half ~ (j+1)*half
#             sub = [row[j*half:(j+1)*half] for row in arr[i*half:(i+1)*half]]
#             result += paper(sub)            # 나눈 부분에 대해 재귀 호출하고 결과 이어붙이기

#     result += ")"                           # 괄호 닫기
#     return result                           # 결과 문자열 반환

# print(paper(listt))                         # 최종 결과 출력


            
        

