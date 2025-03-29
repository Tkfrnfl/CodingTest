# -*- coding:utf-8 -*-
import sys
from collections import deque
input = sys.stdin.readline

def can_reach(n, rooms):
    # 시작점에서부터 각 방까지의 금화 상태
    money = [-float('inf')] * (n + 1)
    money[1] = 0  # 시작 방 금화 0으로 설정

    # BFS를 사용하여 경로 탐색
    q = deque([1])
    visited = [[False] * 1001 for _ in range(n + 1)]  # 방문 체크(방 번호, 금화 상태)
    visited[1][0] = True

    while q:
        cur = q.popleft()
        room_type, cost, *next_rooms = rooms[cur - 1]
        cost = int(cost)

        # 현재 방의 금화 상태 처리
        current_money = money[cur]

        # 레프리콘 방이면 최소 금액 보장
        if room_type == 'L' and current_money < cost:
            current_money = cost

        # 트롤 방이면 금화 소모
        if room_type == 'T' and current_money < cost:
            continue
        elif room_type == 'T':
            current_money -= cost

        # 도착지(n번 방)에 도달한 경우
        if cur == n:
            return "Yes"

        # 다음 방으로 이동
        for next_room in map(int, next_rooms):
            if next_room == 0:
                continue

            # 더 많은 금액으로 방문할 때만 큐에 추가
            # 즉, 재방문은 가능하지만 보유금액이 다른상태
            if current_money > money[next_room]:
                money[next_room] = current_money
                if not visited[next_room][current_money]:
                    visited[next_room][current_money] = True
                    q.append(next_room)

    return "No"

if __name__ == "__main__":
    results = []

    while True:
        n = int(input())
        if n == 0:
            break

        rooms = [input().strip().split() for _ in range(n)]
        result = can_reach(n, rooms)
        results.append(result)

    print("\n".join(results))
