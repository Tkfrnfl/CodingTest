# -*- coding:utf-8 -*-
from collections import deque

if __name__ == "__main__":
    w, h = map(int, input().split())
    array = []

    for _ in range(h):
        array.append(list(input()))

    # 두 'C'의 좌표를 저장하기 위한 리스트
    lasers = []
    
    # 지도를 탐색하여 두 'C'의 좌표를 저장
    for i in range(h):
        for j in range(w):
            if array[i][j] == 'C':
                lasers.append((i, j))

    start_x, start_y = lasers[0]
    target_x, target_y = lasers[1]

    # 방향 벡터 설정
    xx = [-1, 1, 0, 0]
    yy = [0, 0, -1, 1]
    visited = [[(float('inf'), -1) for _ in range(w)] for _ in range(h)] # 최소 거울 사용 횟수를 기록할 visited 리스트
    def bfs(x, y):
        # 큐에 (x, y, 방향, 거울 사용 횟수) 저장
        q = deque()
        visited[x][y] = (0,-1)  # 시작점은 0개 거울로 방문

        for i in range(4):  # 시작점에서 4방향으로 출발
            q.append((x, y, i, 0))  # x, y, 방향 i, 거울 사용 횟수 0

        while q:
            a, b, d, d_num = q.popleft()

            # 현재 노드와 연결된 이웃 노드 탐색
            for i in range(4):
                x_ = a + xx[i]
                y_ = b + yy[i]

                if 0 <= x_ < h and 0 <= y_ < w and array[x_][y_] != '*':
                    new_d_num = d_num
                    if d != i:  # 방향이 바뀌면 거울 추가
                        new_d_num += 1

                    # 더 적은 거울로 도달할 수 있는 경우에만 큐에 추가
                    if visited[x_][y_][0] > new_d_num or (visited[x_][y_][0] == new_d_num and visited[x_][y_][1]!=i):
                        visited[x_][y_] = (new_d_num,i)
                        q.append((x_, y_, i, new_d_num))

    # BFS로 탐색 시작
    bfs(start_x, start_y)

   # 결과 출력
    if visited[target_x][target_y][0] == float('inf'):
        print(-1)  # 도달 불가능한 경우
    else:
        print(visited[target_x][target_y][0])
