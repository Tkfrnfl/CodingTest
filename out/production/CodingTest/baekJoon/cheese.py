#-*- coding:utf-8 -*-
import sys


if __name__=="__main__":
    n,m=map(int,input().split())
    sys.setrecursionlimit(2500)
    array= []

    for i in range(n):
        array.append(list(map(int,input().split())))

    array_in=[[0 for j in range(m)] for i in range(n)]
    visited=[[0 for j in range(m)] for i in range(n)]
    stack=[]

    yy=[1,-1,0,0]
    xx=[0,0,1,-1]
    # 2칸 내부에 있는 빈공간을 외부, 내부로 나누기 
    

    def dfs(y,x):
        visited[y][x]=1
        tmp=0

        stack.append((y,x))
 
        for i in range(4):
            tmpy=y+yy[i]
            tmpx=x+xx[i]

            if 0<=tmpy<n and 0<=tmpx<m and visited[tmpy][tmpx]==0:
                if array[tmpy][tmpx]==1:
                    continue
                else:
                    if tmpy==1 or tmpy==n-2 or tmpx==1 or tmpx==m-2:
                        tmp='o'
                        return 'o'
                    else:
                        tmp=dfs(tmpy,tmpx)
                       
        if tmp =='o':
            return 'o'
        else:
            return 'b'                
    
    def melt_check(y,x):
        #print(array_in)
        open_stack=0

        for i in range(4):
            tmpy=y+yy[i]
            tmpx=x+xx[i]

            if 0<=tmpy<n and 0<=tmpx<m and array_in[tmpy][tmpx]==0 and array[tmpy][tmpx]==0:
                open_stack+=1

        if open_stack>=2:
            return 'm'
        else:
            return        
                
    def in_check():
        global stack
        for i in range(2,n-2):
            for j in range(2,m-2):
                if array[i][j]==0 and visited[i][j]==0:
                    tmp=dfs(i,j)
                    if tmp=='b':
                        
                        while stack:
                            a,b=stack.pop()
                            array_in[a][b]=1
                    else:
                        stack=[]    

    all_melt=1
    ans=0
    while all_melt==1:                
        all_melt=0
        ans+=1
        array_in=[[0 for j in range(m)] for i in range(n)]
        visited=[[0 for j in range(m)] for i in range(n)]
        in_check()
        #print(array_in)
        melt_list=[]

        for i in range(1,n-1):
            for j in range(1,m-1):
                if array[i][j]==1:
                    all_melt=1
                    tmp=melt_check(i,j)
                    if tmp=='m':
                        melt_list.append((i,j))

        while melt_list:
            a,b=melt_list.pop()
            array[a][b]=0

        #print(array)                
    ans-=1    
    print(ans)                    
    #print(array_in)
                   