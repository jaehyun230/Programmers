from collections import deque

import copy

def solution(triangle):
    dist_triangle = copy.deepcopy(triangle)
    q= deque()
    q.append((0, 0))
    dx = [0, 1]
    dy = [1, 1]
    while q :
        y, x = q.popleft()
        for i in range(len(dx)) :
            mx = x+dx[i]
            my = y+dy[i]
            if my == len(triangle) :
                break
            if dist_triangle[my][mx] < dist_triangle[y][x] + triangle[my][mx] :
                dist_triangle[my][mx] = dist_triangle[y][x] + triangle[my][mx]
                q.append((my, mx))

    answer = max(dist_triangle[len(triangle)-1])
    return answer
