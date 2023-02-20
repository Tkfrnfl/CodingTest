#-*- coding:utf-8 -*-


def solution(places):
    answer = [1,1,1,1,1]

    x=[0,0,1,-1,-1,1,-1,1]
    y=[1,-1,0,0,-1,1,1,-1]

    i=0
    while i<5:
        print(i)
        for j in range(5):
            for k in range(5):
                if places[i][j][k]=='P':
                    #print(i,j,k)
                    for l in range(4):
                        xx=k+x[l]
                        yy=j+y[l]
                        if 0<=xx<5 and 0<=yy<5: #상하좌우는 사람있으면 안됨
                            if places[i][yy][xx]=='P':
                                answer[i]=0
                                #print((xx,yy))
                                continue
                            if places[i][yy][xx]=='O':
                                if l==0 and yy+1<5:
                                    if places[i][yy+1][xx]=='P':
                                        answer[i]=0
                                        #print((yy+1,xx))
                                        continue
                                if l==1 and yy-1>=0:
                                    if places[i][yy-1][xx]=='P':
                                        answer[i]=0
                                        #print((yy-1,xx))
                                        continue

                                if l==2 and xx+1<5:
                                    if places[i][yy][xx+1]=='P':
                                        answer[i]=0
                                        #print((yy,xx+1))
                                        continue
                                if l==3 and xx-1>=0:
                                    if places[i][yy][xx-1]=='P':
                                        answer[i]=0
                                        #print((yy,xx-1))
                                        continue    
                    for m in range(4,8):                       
                        
                        xx=k+x[m]
                        yy=j+y[m]     
                        if 0<=xx<5 and 0<=yy<5: #대각선은 벽 체크
                            if places[i][yy][xx]=='P':
                                if m==4:
                                    if places[i][yy][xx+1]!='X'or places[i][yy+1][xx]!='X':
                                        answer[i]=0
                                        #print((xx,yy))
                                        continue
                                if m==5:
                                    if places[i][yy][xx-1]!='X'or places[i][yy-1][xx]!='X':
                                        answer[i]=0
                                        #print((xx,yy))
                                        continue
                                if m==6:
                                    if places[i][yy][xx+1]!='X'or places[i][yy-1][xx]!='X':
                                        answer[i]=0
                                        #print((xx,yy))
                                        continue
                                if m==7:
                                    if places[i][yy][xx-1]!='X'or places[i][yy+1][xx]!='X':
                                        answer[i]=0
                                        #print((xx,yy))
                                        continue     
        i+=1                        
    #print(answer)
    return answer

    
if __name__ == "__main__":
    solution([["OPOPO", "PXPXP", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],["XXXXX", "OPOOO", "POOOO", "OOOOO", "OOOOO"]])