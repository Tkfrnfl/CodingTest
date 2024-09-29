# -*- coding:utf-8 -*-

if __name__ == "__main__":
    n, m, x, y, cmd_n = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    cmd = list(map(int, input().split()))
    ans = []

    # 주사위의 초기 상태 [아래, 북, 동, 서, 남, 위]
    dice = [0, 0, 0, 0, 0, 0]
    nowloc = [x, y]

    def check_valid(i):
        if i == 4:  # 남쪽
            return nowloc[0] + 1 < n
        elif i == 3:  # 북쪽
            return nowloc[0] - 1 >= 0
        elif i == 2:  # 서쪽
            return nowloc[1] - 1 >= 0
        elif i == 1:  # 동쪽
            return nowloc[1] + 1 < m
        return False

    def find():
        global nowloc
        global dice
        for i in cmd:
            if not check_valid(i):
                continue
            
            # 현재 위치에 따라 이동
            if i == 4:  # 남쪽
                nowloc[0] += 1
                if array[nowloc[0]][nowloc[1]] == 0:
                    array[nowloc[0]][nowloc[1]] = dice[0]
                else:
                    dice[0] = array[nowloc[0]][nowloc[1]]
                    array[nowloc[0]][nowloc[1]] = 0
                dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
            elif i == 3:  # 북쪽
                nowloc[0] -= 1
                if array[nowloc[0]][nowloc[1]] == 0:
                    array[nowloc[0]][nowloc[1]] = dice[0]
                else:
                    dice[0] = array[nowloc[0]][nowloc[1]]
                    array[nowloc[0]][nowloc[1]] = 0
                dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
            elif i == 2:  # 서쪽
                nowloc[1] -= 1
                if array[nowloc[0]][nowloc[1]] == 0:
                    array[nowloc[0]][nowloc[1]] = dice[0]
                else:
                    dice[0] = array[nowloc[0]][nowloc[1]]
                    array[nowloc[0]][nowloc[1]] = 0
                dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
            elif i == 1:  # 동쪽
                nowloc[1] += 1
                if array[nowloc[0]][nowloc[1]] == 0:
                    array[nowloc[0]][nowloc[1]] = dice[0]
                else:
                    dice[0] = array[nowloc[0]][nowloc[1]]
                    array[nowloc[0]][nowloc[1]] = 0
                dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

            ans.append(dice[5])  # 윗면 값을 결과에 추가

    find()
    for i in ans:
        print(i)