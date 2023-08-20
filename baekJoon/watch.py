#-*- coding:utf-8 -*-


if __name__ == "__main__":
    a,b=map(int,input().split())
    array=[list(map(int,input().split())) for _ in range(a)]

    ans=1e9
    cctv_loc=[]
    cctv = [
        [],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]],
    ]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(a):
        for j in range(b):
            if array[i][j]!=0 and array[i][j]!=6:
                cctv_loc.append([i,j,array[i][j]])

    def dfs(curr_num):
        global ans,cctv_loc

        count_0=0

        if curr_num==len(cctv_loc):
            for i in range(a):
                for j in range(b):
                    if array[i][j]==0:
                        count_0+=1
            ans=min(ans,count_0)
            return
        
        cctv_x=cctv_loc[curr_num][0]
        cctv_y=cctv_loc[curr_num][1]
        cctv_type=cctv_loc[curr_num][2]

        for cctv_dir in cctv[cctv_type]:
            reset=[]
            for d in cctv_dir: 
                xx=cctv_x
                yy=cctv_y          
                while 1:
                    xx+=dx[d]
                    yy+=dy[d]
                    if 0<=xx<a and 0<=yy<b and array[xx][yy]!=6:
                        reset.append([xx,yy,array[xx][yy]])
                        array[xx][yy]='#'
                    else:
                        break    

            dfs(curr_num+1)
            for x,y,type in reset:
               array[x][y]=type

    dfs(0)
    print(ans)                  