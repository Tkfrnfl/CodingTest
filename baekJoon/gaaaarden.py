# -*- coding:utf-8 -*-
from itertools import combinations
from collections import deque
import copy
import sys

input = sys.stdin.readline

# 입력 받기
n, m, g, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 배양액을 뿌릴 수 있는 위치 저장
land = [(i, j) for i in range(n) for j in range(m) if array[i][j] == 2]

# 방향 벡터 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS로 배양액 전파
def bfs(green_pos, red_pos):
    garden = copy.deepcopy(array)  # 정원 복사본
    queue = deque()  # BFS 탐색을 위한 큐
    time = [[-1] * m for _ in range(n)]  # 배양액이 퍼진 시간을 저장
    color = [[None] * m for _ in range(n)]  # 초록(G)과 빨강(R) 구분

    # 초록색 배양액 배치
    for gx, gy in green_pos:
        queue.append((gx, gy, 'G', 0))
        time[gx][gy] = 0
        color[gx][gy] = 'G'

    # 빨간색 배양액 배치
    for rx, ry in red_pos:
        queue.append((rx, ry, 'R', 0))
        time[rx][ry] = 0
        color[rx][ry] = 'R'

    flower_count = 0  # 꽃 개수

    while queue:
        x, y, c, t = queue.popleft()

        # 꽃이 핀 곳이면 확산 중단
        if color[x][y] == 'F':
            continue

        # 현재 위치에서 네 방향으로 퍼뜨리기
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 내에 있고 배양액을 뿌릴 수 있는 땅이라면
            if 0 <= nx < n and 0 <= ny < m and (garden[nx][ny] == 1 or garden[nx][ny] == 2):
                # 배양액이 아직 퍼지지 않은 경우
                if time[nx][ny] == -1:
                    time[nx][ny] = t + 1
                    color[nx][ny] = c
                    queue.append((nx, ny, c, t + 1))

                # 배양액이 퍼졌는데 다른 색과 같은 시간에 도착했다면 꽃이 핌
                elif time[nx][ny] == t + 1 and color[nx][ny] != c:
                    flower_count += 1
                    color[nx][ny] = 'F'  # 꽃이 핀 자리
                    garden[nx][ny] = 5  # 꽃 표시 (필수는 아님)

    return flower_count

# 배양액을 뿌릴 모든 경우의 수 탐색
max_flowers = 0

# 초록색 배양액 선택
for green_pos in combinations(land, g):
    # 초록색을 제외한 위치에서 빨간색 선택
    remaining_land = [pos for pos in land if pos not in green_pos]

    for red_pos in combinations(remaining_land, r):
        max_flowers = max(max_flowers, bfs(green_pos, red_pos))

print(max_flowers)
