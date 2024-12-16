#-*- coding:utf-8 -*-
from collections import Counter

def ca_direct(ca, r, c, I):
    d_case = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    mn_val = (int(1e9), (0, 0))

    for dc in d_case:
        x = ca[0] + dc[0]
        y = ca[1] + dc[1]

        if 0 <= x < r and 0 <= y < c:

            if (x,y)==I:
                return 'end'

            dis = abs(I[0] - x) + abs(I[1] - y)

            if mn_val[0] > dis:
                mn_val = (dis, (x, y))

    return mn_val            

def game_check(cA):
    loc_count = {}
    for loc in cA:
        if loc in loc_count:
            loc_count[loc] += 1  # 위치별 카운트 증가
        else:
            loc_count[loc] = 1

    # 한 위치에 여러 아두이노가 있으면 제거 (폭발)
    return [loc for loc in cA if loc_count[loc] == 1]

if __name__ == "__main__":
    r, c = map(int, input().split())  
    array = [list(input().strip()) for _ in range(r)]  
    direct = str(input().strip())  
    d_list = [int(di) for di in direct]  

    cA = []  
    I = (0, 0)  

    for i in range(r):
        for j in range(c):
            if array[i][j] == 'I':
                I = (i, j)
            if array[i][j] == 'R':
                cA.append((i, j))

    d_case = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
    proceed_num = 0
    answer=False

    for d in d_list:
        proceed_num += 1

        I = (I[0] + d_case[d - 1][0], I[1] + d_case[d - 1][1])

        if I in cA:
            print(f"kraj {proceed_num}")
            answer =True
            break

        new_cA = []
        for ca in cA:
            mn = ca_direct(ca, r, c, I)
            if mn =='end':
                print(f"kraj {proceed_num}")
                answer =True
                break             
            else:   
                new_cA.append(mn[1])
        if answer:
            break
        cA = game_check(new_cA)  

        if I in cA:
            print(f"kraj {proceed_num}")
            answer =True
            break
    if not answer:
        # 최종 보드 출력
        for i in range(r):
            row = ''
            for j in range(c):
                if (i, j) == I:
                    row += 'I'
                elif (i, j) in cA:
                    row += 'R'
                else:
                    row += '.'
            print(row)

