# -*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(5000)

if __name__ == "__main__":
    n, m= map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    
    ans =0

    # def dfs(x,y,v,num):  # dfs는 시간초과
    #     global n,m,ans
    #     xx=[1,0,0]
    #     yy=[0,-1,1]

    #     v[x][y]= True

    #     if x==n-1 and y==n-1 and num>ans:
    #         ans=max(ans,num)
    #         return
        
    #     for i in range(3):
    #         x_=x+xx[i]
    #         y_=y+yy[i]

    #         if 0<=x_<n and 0<=y_<m and not v[x_][y_]:

    #             num+=array[x_][y_]
    #             dfs(x_,y_,v,num)
    #             v[x_][y_]=False
    #             num-=array[x_][y_]

    # visited=[[False]*m for _ in range(n)]
    # dfs(0,0,visited,array[0][0])

    # print(ans)                


    dp = [[-float('inf')] * m for _ in range(n)]
    dp[0][0] = array[0][0] 

    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + array[0][j]

    # DP 계산
    for i in range(1, n):
        # 왼쪽에서 오른쪽으로 진행
        left_to_right = [-float('inf')] * m
        left_to_right[0] = dp[i - 1][0] + array[i][0]
        for j in range(1, m):
            left_to_right[j] = max(left_to_right[j - 1], dp[i - 1][j]) + array[i][j] # 옆에서 오거나, 위에서 오는것

        # 오른쪽에서 왼쪽으로 진행
        right_to_left = [-float('inf')] * m
        right_to_left[m - 1] = dp[i - 1][m - 1] + array[i][m - 1]
        for j in range(m - 2, -1, -1):
            right_to_left[j] = max(right_to_left[j + 1], dp[i - 1][j]) + array[i][j]

        # 두 가지 진행 방식에서 최대 값 선택
        for j in range(m):
            dp[i][j] = max(left_to_right[j], right_to_left[j])

  
    print(dp[n - 1][m - 1])