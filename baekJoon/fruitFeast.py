# -*- coding:utf-8 -*-
from collections import deque

if __name__ == "__main__":
    t, a, b = map(int, input().split())

    ans = 0
    q = deque([0])
    visited = set([0]) 

    while q:
        p = q.popleft()
        ans = max(ans, p)

        if p > t:
            continue

        if ans == t:
            break

        if p + a <= t and (p + a) not in visited:
            visited.add(p + a)
            q.append(p + a)

        if p + b <= t and (p + b) not in visited:
            visited.add(p + b)
            q.append(p + b)

        if p // 2 not in visited:
            visited.add(p // 2)
            q.append(p // 2)

    print(ans)
