#-*- coding:utf-8 -*-

if __name__=="__main__":
    n=int(input())

    array=[0]*1002

    for i in range(n):
        l,h = map(int,input().split())
        array[l]=h

    max_pillar=max(array)
    max_index=array.index(max_pillar)

    width=0
    tmp_max=0
    tmp_i=0
    tmp_now=-1
    for i in range(max_index):  #시작점 찾기
        if array[i]!=0:
            tmp_i=i
            break
    if tmp_i==0:
        tmp_i=max_index    
    tmp_max=array[tmp_i]    

    for i in range(tmp_i,max_index+1): #앞에서 max까지
        tmp_now+=1
        if array[i]!=0:
            if array[i]>tmp_max:
                width+=(tmp_max*tmp_now)
                tmp_max=array[i]
                tmp_now=0 
            #print(width)    
    array=array[max_index:]   
    array.reverse()         


    tmp_max=0
    tmp_i=0
    tmp_now=-1
    max_index=array.index(max_pillar)
    for i in range(len(array)):  #시작점 찾기
        if array[i]!=0:
            tmp_i=i
            break
    if tmp_i==0:
        tmp_i=max_index    
    tmp_max=array[tmp_i]   

    for i in range(tmp_i,len(array)): # 리버스 한것 앞에서 max까지
        tmp_now+=1
        if array[i]!=0:
            if array[i]>=tmp_max:
                width+=(tmp_max*tmp_now)
                tmp_max=array[i]
                tmp_now=0 
            #print(width)  
    width+=max_pillar

    print(width)            

