from itertools import combinations
from collections import deque

def down(now_arr):
    for i in range(n - 2, -1, -1):
        now_arr[i + 1] = now_arr[i][:]
    now_arr[0] = [0] * m
    return now_arr

def simulate(archers):
    now_arr = [row[:] for row in arr]  # 현재 상태 복사
    kill_mark = 0
    
    for _ in range(n):
        targets = []  # 현재 턴에 죽일 적
        for archer in archers:
            queue = deque([(n - 1, archer, 0)])  # (x, y, depth)
            visited = [[False] * m for _ in range(n)]  # 방문 배열 초기화
            found = False
            
            while queue and not found:
                x, y, depth = queue.popleft()
                
                if depth > d:
                    break
                
                if now_arr[x][y] == 1:  # 적을 발견
                    targets.append((x, y))  # 적의 위치 추가
                    found = True
                    break
                
                # 왼쪽, 위쪽, 아래, 오른쪽 탐색
                if y - 1 >= 0 and not visited[x][y - 1]:
                    visited[x][y - 1] = True
                    queue.append((x, y - 1, depth + 1))
                if x - 1 >= 0 and not visited[x - 1][y]:
                    visited[x - 1][y] = True
                    queue.append((x - 1, y, depth + 1))
                if x + 1 < n and not visited[x + 1][y]:
                    visited[x + 1][y] = True
                    queue.append((x + 1, y, depth + 1))    
                if y + 1 < m and not visited[x][y + 1]:
                    visited[x][y + 1] = True
                    queue.append((x, y + 1, depth + 1))
        
        # 적을 제거
        unique_targets = set(targets)
        for target in unique_targets:
            x, y = target
            if now_arr[x][y] == 1:  
                now_arr[x][y] = 0
                kill_mark += 1
        
        # 적 이동
        now_arr = down(now_arr)
    
    return kill_mark

if __name__ == "__main__":
    n, m, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    mx = 0
    for archers in combinations(range(m), 3):
        mx = max(mx, simulate(archers))
    
    print(mx)
