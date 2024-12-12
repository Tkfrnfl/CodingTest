# -*- coding:utf-8 -*-
import heapq

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = []

    for _ in range(n):
        array.append(list(map(int, input().strip())))
    ans = 0 

    max_height = max(map(max, array))
    visited = [[[False] * (max_height + 1) for _ in range(m)] for _ in range(n)]

    def bfs(x, y, h):
        global n, m, array, visited
        hq = []
        heapq.heappush(hq, (x, y))
        water_count = 1  # 물을 채울 수 있는 칸 수
        is_enclosed = True  # 물이 완전히 둘러싸여 있는지 여부

        while hq:
            a, b = heapq.heappop(hq)

            if visited[a][b][h]:
                continue
            visited[a][b][h] = True

            # 상하좌우 탐색
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny][h]:
                        if array[nx][ny] < h:  # 물을 채울 수 있는 칸이라면
                            water_count += 1
                            heapq.heappush(hq, (nx, ny))
                        elif array[nx][ny] >= h:
                            # 주변에 벽이 있어 물이 막힘
                            continue
                else:
                    # 외곽이거나 물이 유출될 수 있는 칸인 경우
                    is_enclosed = False

        # 물이 유출되지 않는다면 water_count 반환, 유출되면 0 반환
        return water_count if is_enclosed else 0

    # 높이별로 가능한 물 양을 계산
    for h in range(2, max_height + 1):
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if array[i][j] < h and not visited[i][j][h]:  # 물을 채울 수 있는 칸이라면
                    ans += bfs(i, j, h)

    print(ans)
