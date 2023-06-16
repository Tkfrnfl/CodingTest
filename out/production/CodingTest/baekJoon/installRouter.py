#-*- coding:utf-8 -*-
import math

if __name__ == "__main__":
    n,c = map(int, input().split())
    array=[int(input()) for _ in range(n)]
    array.sort()
    total=[0]*200000
    
    for i in range(n):
        total[array[i]]=1

    avg=(array[n-1]-array[0])/c
    dist=199999
    next=array[0]
    #print('---')   
    for j in range(c-1):
        tmp=next+avg

        #가장 가까운 존재하는 집 찾기
        num=-1
        
        #print(next)
        while True:
            num+=1
            tmp_ceil=tmp+num
            tmp_floor=tmp-num
            ceil= math.ceil(tmp_ceil)
            floor=math.floor(tmp_floor)

            # #바닥 천장 둘다 존재
            # if total[ceil]==1 and total[floor]==1:
            #     #천장에 공유기 설치     
            #     dist=min(dist,ceil-next)
            #     next=ceil
            #     break
            #천장 존재    
            if total[ceil]==1:
                dist=min(dist,ceil-next)
                next=ceil
                break
            #바닥 존재    
            elif total[floor]==1:
                dist=min(dist,floor-next)
                next=floor
                break
    #print('---')        
    print(dist)
    
