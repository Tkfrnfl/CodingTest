if __name__ == "__main__":
    r,c = map(int, input().split())
    arr = [list(input())for _ in range(r)]

   
    answer =0
    alpha =[]
    for i in range(r):
        for j in range(c):
            alpha.append(arr[i][j])

    mx= len(set(alpha))  

    visit = 1<<(ord(arr[0][0])-ord('A'))

    def dfs(a,b,visited,ans):
        global answer,mx
        x=[1,-1,0,0]
        y=[0,0,1,-1]

        answer= max(answer,ans)
        if answer== mx:
            return
        for i in range(4):
            xx=x[i]+a
            yy=y[i]+b

            if  0 <= xx < r and 0 <= yy < c and not visited & 1<<(ord(arr[xx][yy])-ord('A')):

                visited ^= (1<<(ord(arr[xx][yy])-ord('A')))
                dfs(xx,yy,visited,ans+1)
                visited ^= (1<<(ord(arr[xx][yy])-ord('A')))  



    dfs(0,0,visit,1)

    print(answer)


