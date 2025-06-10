from collections import deque
import sys
input_ = sys.stdin.readline

N = int(input_())
graph = {}

for _ in range(N):
    line = input_().split()
    parent = line[0]
    child = line[1:]
    graph[parent] = child
    