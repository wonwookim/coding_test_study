import math
N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

new_scores = []

for i in range(N) :
  scores[i] = scores[i] / max_score * 100
  new_scores.append(scores[i])

print(sum(new_scores) / len(new_scores))