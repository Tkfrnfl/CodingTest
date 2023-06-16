if __name__ == "__main__":
    global ans
    n,m = map(int, input().split())
    array=[list(map(int, input().split())) for _ in range(n)]

    x=[0,0,1,-1]
    y=[1,-1,0,0]
    ans=0
    

    def check_tet(i,j,checked,num,sum):
        #print(i,j)
        global ans
        for k in range(4):
            xx=i+x[k]
            yy=j+y[k]

            if 0<=xx<n and 0<=yy<m and checked[xx][yy]==0:    
                checked[xx][yy]=1
                num+=1
                sum+=array[xx][yy]
                if num==4:
                    ans=max(ans,sum)
                else:
                    check_tet(xx,yy,checked,num,sum)    
                checked[xx][yy]=0
                num-=1
                sum-=array[xx][yy]
    checked=[[0]*m for i in range(n)]
    def h(i,j):
        global ans
        u=i-1
        d=i+1
        r=j+1
        l=j-1
        if d<n and 0<=l and r<m:
            sum=array[i][j]+array[d][j]+array[i][l]+array[i][r]
            ans=max(sum,ans)
        if 0<=u and 0<=l and r<m:
            sum=array[i][j]+array[u][j]+array[i][l]+array[i][r]
            ans=max(sum,ans)
        if 0<=u and d<n and r<m:
            sum=array[i][j]+array[u][j]+array[d][j]+array[i][r]
            ans=max(sum,ans)      
        if 0<=u and d<n and 0<=l:
            sum=array[i][j]+array[u][j]+array[d][j]+array[i][l]
            ans=max(sum,ans)        
    for i in range(n):
        for j in range(m):
            
            checked[i][j]=1
            #ans=max(ans,check_tet(i,j,checked,1,array[i][j]))
            # print('----')
            # print(i,j)
            # print('----')
            check_tet(i,j,checked,1,array[i][j])
            #ㅗ 모양 추가하여 고려
            h(i,j)
            checked[i][j]=0

    print(ans)        


                