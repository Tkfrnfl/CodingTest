from itertools import combinations

def checkWall(num):
    q = num // 2
    r = num % 2

    wall_arr = []
    while q > 0:
        wall_arr.append(r)
        r = q % 2
        q = q // 2
    wall_arr.append(r)

    while len(wall_arr) < 4:
        wall_arr.append(0)

    return wall_arr

def dfs(x, y, wall_info, e_castle):
    global array, visited, n, m

    if visited[x][y]:
        return

    visited[x][y] = True

    xx = [0, -1, 0, 1]
    yy = [-1, 0, 1, 0]

    for k in range(4):
        x_ = x + xx[k]
        y_ = y + yy[k]

        if wall_info[k] == 0 and 0 <= x_ < m and 0 <= y_ < n and not visited[x_][y_]:
            e_castle.append((x_, y_))
            dfs(x_, y_, checkWall(array[x_][y_]), e_castle)

    return e_castle

def findConnect(a, b, castle):
    global array, visited, n, m

    for co in castle[a]:
        xx = [0, -1, 0, 1]
        yy = [-1, 0, 1, 0]

        for k in range(4):
            x_ = co[0] + xx[k]
            y_ = co[1] + yy[k]

            # 벽 정보를 다시 계산하여 사용
            wall_info = checkWall(array[co[0]][co[1]])

            if wall_info[k] == 1 and 0 <= x_ < m and 0 <= y_ < n and (x_, y_) in castle[b]:
                return True
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(m)]

    visited = [[False] * n for _ in range(m)]

    castle = []

    # 모든 좌표에 대해 DFS 실행
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                wall_info = checkWall(array[i][j])
                castle_room = dfs(i, j, wall_info, [(i, j)])
                if castle_room:  # None 체크
                    castle.append(castle_room)

    room_size = []

    for i in castle:
        room_size.append(len(i))

    comb = list(combinations(range(len(room_size)), 2))

    mx_sum = 0

    for com in comb:
        if findConnect(com[0], com[1], castle):
            mx_sum = max(mx_sum, room_size[com[0]] + room_size[com[1]])

    print(len(room_size))  # 방의 개수
    print(max(room_size))  # 가장 넓은 방의 넓이
    print(mx_sum)          # 벽을 하나 제거했을 때 가장 넓은 방의 크기
