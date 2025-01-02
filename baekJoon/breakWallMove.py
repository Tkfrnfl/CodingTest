from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = [list(input().strip()) for _ in range(n)]

    if array[0][0] == '1' or array[n-1][m-1] == '1':
        print(-1)
        exit()

    # BFS를 위한 큐와 방문 배열
    queue = deque([(0, 0, 0, 1)])  # (x, y, wcnt, dist)
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True

    # 방향 벡터
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, wcnt, dist = queue.popleft()

        # 도착점 도달 시 종료
        if x == n-1 and y == m-1:
            print(dist)
            exit()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 부수지 않고 이동
                if array[nx][ny] == '0' and not visited[nx][ny][wcnt]:
                    visited[nx][ny][wcnt] = True
                    queue.append((nx, ny, wcnt, dist + 1))

                # 벽을 부수고 이동
                if array[nx][ny] == '1' and wcnt == 0 and not visited[nx][ny][wcnt + 1]:
                    visited[nx][ny][wcnt + 1] = True
                    queue.append((nx, ny, wcnt + 1, dist + 1))

    # 경로를 찾지 못한 경우
    print(-1)
