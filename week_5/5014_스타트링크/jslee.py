#메모리: 81684kb 시간: 572ms


from collections import deque


F, S, G, U, D = map(int, input().split())

def min_button_presses(F, S, G, U, D):
    visited = [False] * (F + 1)
    dist = [0] * (F + 1)

    queue = deque([S])
    visited[S] = True

    while queue:
        current = queue.popleft()
        for next_floor in [current + U, current - D]: # 위아래로 움직이기
            if 1 <= next_floor <= F and not visited[next_floor]:
                visited[next_floor] = True
                dist[next_floor] = dist[current] + 1
                queue.append(next_floor)

    return dist[G] if visited[G] else "use the stairs"


print(min_button_presses(F, S, G, U, D))
