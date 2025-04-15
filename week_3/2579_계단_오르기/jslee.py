Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... input = sys.stdin.readlines
... 
... # 입력 처리
... lines = input()
... n = int(lines[0].strip())
... score = [int(x.strip()) for x in lines[1:]]
... 
... 
... '''
... score = []
... 
... for x in lines[1:]:
...     x = x.strip()    
...     num = int(x)      
...     score.append(num)  
... '''
... 
... # DP 배열
... dp = [0] * n
... 
... # 초기값
... dp[0] = score[0]
... if n >= 2:
...     dp[1] = score[0] + score[1]
... if n >= 3:
...     dp[2] = max(score[0] + score[2], score[1] + score[2])
... 
... # 점화식
... for i in range(3, n):
...     dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
... 
... 
