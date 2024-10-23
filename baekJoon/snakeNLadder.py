from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())

    # 사다리와 뱀 정보를 담을 배열
    arr = [0] * 101

    # 사다리 정보 입력
    for _ in range(n):
        x, y = map(int, input().split())
        arr[x] = y

    # 뱀 정보 입력
    for _ in range(m):
        u, v = map(int, input().split())
        arr[u] = v

    # BFS를 위한 큐 (현재 위치, 주사위를 굴린 횟수)
    q = deque([(1, 0)])
    visited = [False] * 101
    visited[1] = True

    while q:
        now, rolls = q.popleft()

        # 주사위를 굴려서 1부터 6까지 이동
        for dice in range(1, 7):
            next_pos = now + dice
            if next_pos > 100:
                continue
            
            # 사다리나 뱀이 있는 경우 해당 위치로 이동
            if arr[next_pos] != 0:
                next_pos = arr[next_pos]
            
            # 100번 칸에 도착하면 정답 출력
            if next_pos == 100:
                print(rolls + 1)
                exit()
            
            # 아직 방문하지 않은 칸이라면 큐에 추가
            if not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, rolls + 1))
