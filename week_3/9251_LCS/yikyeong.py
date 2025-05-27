# LCS(Longest Common Subsequence, 최장 공통 부분 수열)
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
# 입력: 첫째 줄과 둘째 줄에 두 문자열이 주어진다.
# 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
# 출력: 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

# 메모리 57628KB, 시간 492ms
# 참고 링크 (다이나믹 프로그래밍, DP)
# https://hongjw1938.tistory.com/47
# https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-9251-LCS-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://www.youtube.com/watch?v=EAXDUxVYquY
# 유사문제: 백준 9252_LCS2, 5582_공통 부분 문자열

arr1 = list(input())
arr2 = list(input())

dp = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]
dp[0][0] = 0

for i in range(1, len(arr1) + 1):
    for j in range(1, len(arr2) + 1):

        if arr1[i-1] == arr2[j-1]: # 해당 자리의 알파벳이 같을 때
            dp[i][j] = dp[i-1][j-1] + 1 # 이전 상태의 dp 값에서 1을 더함 (같은 부분이 하나 늘어났다는 뜻)

        else: # arr1[i-1] != arr2[j-1] # 알파벳이 다를 때
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 바로 윗 칸 또는 왼쪽 칸의 dp 값 중 최댓값을 할당함
            # dp[i-1][j-1]의 값을 가져오면 공통 부분 길이를 손해볼 수 있기 때문
            # 예를 들어, dp[i-1][j-1]가 2, dp[i-1][j]가 2, dp[i][j-1]은 3인 경우,
            # dp[i-1][j-1]의 값인 2를 가져오게 되면 실제로 최장 길이인 3을 간과함

print(dp[-1][-1])