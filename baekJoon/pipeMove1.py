# if __name__ == "__main__":
#     n = int(input())
#     array=[list(map(int, input().split())) for _ in range(n)]

#     first=[(0,0),(0,1)]

#     visited =[[0 for _ in range(n)] for _ in range(n)]

#     visited[0][1] =1
    
    
#     def find(now):
#         global array,n
#         print(now)
#         if now[1][0] ==n-1 and now[1][1]== n-1:
#             return
        
#         if now[0][0] == now[1][0] : #가로
#             if now[1][1]+1<n and array[now[1][0]][now[1][1]+1]==0:
#                 visited[now[1][0]][now[1][1]+1]+=visited[now[1][0]][now[1][1]]
#                 find([(now[0][0],now[0][1]+1),(now[1][0],now[1][1]+1)])

#             if now[1][1]+1<n and now[1][0]+1<n and array[now[1][0]+1][now[1][1]+1]==0:
#                 visited[now[1][0]+1][now[1][1]+1]+=visited[now[1][0]][now[1][1]]
#                 find([(now[0][0],now[0][1]+1),(now[1][0]+1,now[1][1]+1)])

#         if now[0][0] != now[1][0] and now[0][1] != now[1][1]: #대각
#             if now[1][1]+1<n and array[now[1][0]][now[1][1]+1]==0:
#                 visited[now[1][0]][now[1][1]+1]+=visited[now[1][0]][now[1][1]]
#                 find([(now[0][0]+1,now[0][1]+1),(now[1][0],now[1][1]+1)])

#             if now[1][1]+1<n and now[1][0]+1<n and array[now[1][0]+1][now[1][1]+1]==0:
#                 visited[now[1][0]+1][now[1][1]+1]+=visited[now[1][0]][now[1][1]]
#                 find([(now[0][0]+1,now[0][1]+1),(now[1][0]+1,now[1][1]+1)])      

#             if now[1][0]+1<n and array[now[1][0]+1][now[1][1]]==0:
#                 visited[now[1][0]+1][now[1][1]]+=visited[now[1][0]][now[1][1]]
#                 find([(now[0][0]+1,now[0][1]+1),(now[1][0]+1,now[1][1])])               

#         if now[0][1] == now[1][1] : #세로
#             if now[1][0]+1<n and array[now[1][0]+1][now[1][1]]==0:
#                 visited[now[1][0]+1][now[1][1]]+=visited[now[1][0]][now[1][1]]
#                 find([(now[0][0]+1,now[0][1]),(now[1][0]+1,now[1][1])])

#             if now[1][1]+1<n and now[1][0]+1<n and array[now[1][0]+1][now[1][1]+1]==0:
#                 visited[now[1][0]+1][now[1][1]+1]+=visited[now[1][0]][now[1][1]]
#                 find([(now[0][0]+1,now[0][1]),(now[1][0]+1,now[1][1]+1)])
#         return
#     find(first)
#     print(visited[n-1][n-1])
if __name__ == "__main__":
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]

    # 3차원 DP 배열 초기화: dp[r][c][direction]
    # direction: 0 (가로), 1 (세로), 2 (대각선)
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1  # 시작 위치 (1, 2)에서 가로 방향으로 초기화

    for r in range(n):
        for c in range(1, n):
            if array[r][c] == 1:
                continue  # 벽인 경우는 건너뜀
            
            # 가로로 놓여 있는 경우 (→)
            if c - 1 >= 0:
                dp[r][c][0] += dp[r][c - 1][0]  # 이전 칸이 가로 방향
                dp[r][c][0] += dp[r][c - 1][2]  # 이전 칸이 대각선 방향

            # 세로로 놓여 있는 경우 (↓)
            if r - 1 >= 0:
                dp[r][c][1] += dp[r - 1][c][1]  # 이전 칸이 세로 방향
                dp[r][c][1] += dp[r - 1][c][2]  # 이전 칸이 대각선 방향

            # 대각선으로 놓여 있는 경우 (↘)
            if r - 1 >= 0 and c - 1 >= 0:
                if array[r - 1][c] == 0 and array[r][c - 1] == 0:
                    dp[r][c][2] += dp[r - 1][c - 1][0]  # 이전 칸이 가로 방향
                    dp[r][c][2] += dp[r - 1][c - 1][1]  # 이전 칸이 세로 방향
                    dp[r][c][2] += dp[r - 1][c - 1][2]  # 이전 칸이 대각선 방향

    # 최종적으로 (n-1, n-1)에서 가로, 세로, 대각선으로 도달한 모든 경우의 수의 합
    result = dp[n - 1][n - 1][0] + dp[n - 1][n - 1][1] + dp[n - 1][n - 1][2]
    print(result)
