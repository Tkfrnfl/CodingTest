import sys

sys.setrecursionlimit(10**6)  # 최대 재귀 깊이 설정

def solve():
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    
    boomerangs = [
        [(0, 0), (-1, 0), (0, -1)],  # ㄴ 모양
        [(0, 0), (-1, 0), (0, 1)],   # ㄱ 모양
        [(0, 0), (1, 0), (0, -1)],   # ┗ 모양
        [(0, 0), (1, 0), (0, 1)]     # ┛ 모양
    ]
    
    visited = [[False] * m for _ in range(n)]
    max_score = 0

    # 백트래킹 + DFS 탐색
    def dfs(x, y, score):
        nonlocal max_score
        
        # 종료 조건
        if x == n:  # 마지막 행을 넘어가면
            max_score = max(max_score, score)
            return
        
        # 다음 좌표 계산 (y가 m-1이면 x를 하나 증가시키고 y는 0으로 리셋)
        nx, ny = (x, y + 1) if y + 1 < m else (x + 1, 0)
        
        # 부메랑을 놓지 않는 경우
        dfs(nx, ny, score)
        
        # 부메랑을 놓는 경우 탐색
        for boomerang in boomerangs:
            positions = []
            total_strength = 0
            valid = True

            for dx, dy in boomerang:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    positions.append((nx, ny))
                    total_strength += array[nx][ny] * (2 if (dx, dy) == (0, 0) else 1)
                else:
                    valid = False
                    break

            if valid:
                # 부메랑을 놓을 수 있다면 방문 표시
                for px, py in positions:
                    visited[px][py] = True

                # 재귀 호출
                dfs(nx, ny, score + total_strength)

                # 백트래킹: 방문 표시 원상복구
                for px, py in positions:
                    visited[px][py] = False

    # DFS 시작
    dfs(0, 0, 0)

    print(max_score)

if __name__ == "__main__":
    solve()
