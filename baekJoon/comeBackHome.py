# -*- coding:utf-8 -*-
from collections import deque

if __name__ == "__main__":
    r,c,k = map(int, input().split())
    array = [list(input().strip()) for _ in range(r)]

    ans=0

    def dfs(x,y,dist,visited):
        global ans
        xx=[1,-1,0,0]
        yy=[0,0,1,-1]
        visited[x][y]=True

        if dist == k and x == 0 and y == c - 1:
            ans += 1
            visited[x][y] = False  
            return

        for i in range(4):
            nx=x+xx[i]
            ny=y+yy[i]

            if 0 <= nx < r and 0 <= ny < c and array[nx][ny] != 'T' and not visited[nx][ny]:
                dfs(nx, ny, dist + 1, visited)
        
        visited[x][y]=False         

    visited=[[False]*c for _ in range(r)]
    dfs(r-1,0,1,visited)

    print(ans)