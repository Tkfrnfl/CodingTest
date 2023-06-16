import sys
sys.setrecursionlimit(10**5)

if __name__ == "__main__":
    n,m = map(int, input().split())
    r,c,d = map(int, input().split())
    array=[list(map(int, input().split())) for _ in range(n)]

    ans=0
    di_list=[(-1,0),(0,1),(1,0),(0,-1)]

    checked=[[0]*m for i in range(n)]
    def check(y,x,direct):
        global ans
        # print(y,x)
        # print(ans)
        if array[y][x]==0 and checked[y][x]==0:
            checked[y][x]=1
            ans+=1

        new_di=direct-1

        if new_di<-4:
            new_di+=4
        if direct<-2:
            direct+=4    
        new_y=y+di_list[new_di][0]
        new_x=x+di_list[new_di][1]

        uy,ux=y+di_list[0][0],x+di_list[0][1]
        ry,rx=y+di_list[1][0],x+di_list[1][1]
        dy,dx=y+di_list[2][0],x+di_list[2][1]
        ly,lx=y+di_list[3][0],x+di_list[3][1]

        if (array[uy][ux]==1 or checked[uy][ux]==1) and \
            (array[ry][rx]==1 or checked[ry][rx]==1) and \
                (array[dy][dx]==1 or checked[dy][dx]==1) and\
                    (array[ly][lx]==1 or checked[ly][lx]==1):
                        tmp_y=y+di_list[direct-2][0]
                        tmp_x=x+di_list[direct-2][1]
                        if array[tmp_y][tmp_x]==1: # 뒤까지다 벽이라 못가면
                            return
                        else:
                            check(tmp_y,tmp_x,direct) # 뒤는 갈수있다면   
                            return
        # 갈수 있다면 방향, 위치바꿔 가고                    
        if array[new_y][new_x]==0 and checked[new_y][new_x]==0: 
            check(new_y,new_x,new_di)
        else:   #아니면 방향만 바꿔 재탐색
            check(y,x,new_di)     
        return
    check(r,c,d)

    print(ans)    