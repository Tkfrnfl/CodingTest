#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
answer = 999999
visited=[]
def solution(board):
    global visited
    n=len(board[0])
    xx=[1,-1,0,0] #세로
    yy=[0,0,1,-1] #가로
    visited=[[999999 for j in range(n)] for i in range(n)]

    def dfs(x,y,corner,fee):
        global answer
        global visited
        visited[x][y]=min(visited[x][y],fee)
        print(visited)
        #print((x,y))
        if x==n-1 and y==n-1:
            answer=min(answer,fee)
            return
        block=True    
        for i in range(4):
            # if(x,y)==(0,6):
            #     print(i)
            x=x+xx[i]
            y=y+yy[i]

            if 0<=x<n and 0<=y<n and board[x][y]==0:
                block=False
                #col, row, 구별
                if (i==0 or i==1)and corner==-1: ## 처음>세로
                    fee+=100
                    if visited[x][y]>fee:
                        dfs(x,y,1,fee)
                elif (i==2 or i==3)and corner==-1: ## 처음>가로
                    fee+=100
                    if visited[x][y]>fee:
                        dfs(x,y,1,fee)   
                elif (i==0 or i==1)and corner==1: ##세로>세로
                    fee+=100
                    if visited[x][y]>fee:
                        dfs(x,y,1,fee)
                elif (i==2 or i==3)and corner==1: ##세로>가로
                    fee+=500
                    if visited[x][y]>fee:
                        dfs(x,y,1,fee)  
                elif (i==0 or i==1)and corner==0: ##가로>세로
                    fee+=500
                    if visited[x][y]>fee:
                        dfs(x,y,1,fee)
                elif (i==2 or i==3)and corner==0: ##가로>가로
                    fee+=100
                    if visited[x][y]>fee:
                        dfs(x,y,1,fee)  

        # if block:
        #     return      

    #print(visited)       
    dfs(0,0,-1,0)                        
    print(answer)
    return answer

if __name__ == "__main__":
    solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])