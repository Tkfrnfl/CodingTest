import math

if __name__ == "__main__":
    global ans
    r,c,t = map(int, input().split())
    array=[list(map(int, input().split())) for _ in range(r)]

    cleaner=[]

    for i in range(r):
        for j in range(c):
            if array[i][j]==-1:
                cleaner.append([i,j])

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def spread():

        spread_save=[]
        for i in range(r):
            for j in range(c):
                if array[i][j]>0:

                    spread_num=0
                    for k in range(4):
                        xx=i+dx[k]
                        yy=j+dy[k]

                        if 0<=xx<r and 0<=yy<c and array[xx][yy]!=-1 :    #벽이아니면 확산
                            spread_num+=1
                            # 퍼져나갈값 저장
                            spread_save.append([xx,yy,math.floor(array[i][j]/5)])

                    array[i][j]= array[i][j]- (math.floor(array[i][j]/5)*spread_num)

        #확산된 값 적용
        for x,y,num in spread_save:
            array[x][y]+=num
    for i in range(t):
        spread()

        #위쪽 순환
        ux,uy=cleaner[0]
        for j in range(1,ux):
            array[ux-j][uy]=array[ux-(j+1)][uy]
        for j in range(c-1):
            array[0][j]=array[0][j+1]
        for j in range(0,ux):
            array[j][c-1]=array[j+1][c-1]
        for j in range(c-2):
            array[ux][c-(j+1)]=array[ux][c-(j+2)]
        array[ux][uy+1]=0
        #아래쪽 순환
        dox,doy=cleaner[1]

        for j in range(1,(r-1)-dox):
            array[dox+j][doy]=array[dox+j+1][doy]
        for j in range(c-1):
            array[r-1][j]=array[r-1][j+1]
        for j in range(1,r-dox):
            array[r-j][c-1]=array[r-(j+1)][c-1]
        for j in range(c-2):
            array[dox][c-(j+1)]=array[dox][c-(j+2)]    
        array[dox][doy+1]=0    

    answer=2
    for i in range(r):
        answer+=sum(array[i])
    print(answer)    