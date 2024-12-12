# -*- coding:utf-8 -*-
from collections import deque

def bfs(n, k):
    visited = [False] * (100001)  
    q = deque()
    q.append((n, 0))  
    visited[n] = True  

    while q:
        nn, t = q.popleft()

        if nn == k:
            return t

        # 순간이동 (시간 0초)
        if nn * 2 <= 100000 and not visited[nn * 2]:
            visited[nn * 2] = True
            q.appendleft((nn * 2, t))  # 시간 소요 없음 -> 큐의 앞에 추가

        # -1 또는 +1 이동 (시간 1초)
        for next_nn in (nn - 1, nn + 1):
            if 0 <= next_nn <= 100000 and not visited[next_nn]:
                visited[next_nn] = True
                q.append((next_nn, t + 1))  

    return -1  

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(bfs(n, k))