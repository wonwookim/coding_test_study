#32412KB	60ms
import sys
N = int(sys.stdin.readline().strip())
listt = []
for _ in range(N):
    a = sys.stdin.readline().strip() # 입력 받기기
    b = list(map(int, a.split())) # 공백 제거 및 숫자화
    listt.append(b) # 리스트로 합치기 

result = []
def paper(listt,result):
    answer = listt[0][0]
    same = True
    for i in range(len(listt)):
        for j in range(len(listt)):
            if listt[i][j] != answer:
                same = False
                break
        if same == False:
            break

    if same == True:
        result.append(answer)
        return answer
    else:
        n = int(len(listt) / 2)
        for i in range(2):
            for j in range(2):
                # listt2 = listt[i*n:(i+1)*n][j*n:(j+1)*n] # 행으로만 두번 슬라이싱 하게 된다다
                listt2 = [row[j*n:(j+1)*n] for row in listt[i*n:(i+1)*n]]
                paper(listt2,result)
    
paper(listt,result)

print(result.count(0))   
print(result.count(1))   
            
        

