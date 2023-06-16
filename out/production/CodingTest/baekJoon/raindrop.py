#-*- coding:utf-8 -*-


if __name__ == "__main__":
    h,w=map(int,input().split())
    array=list(map(int,input().split()))

    tmp_max=max(array)
    tmp_max_index=array.index(tmp_max)

    first=0
    rain=0

    for i in range(0,tmp_max_index):    #가장큰것 기준 좌우 체크
        if array[i]>first:
            first=array[i]
        else:
            tmp=first-array[i]
            rain+=tmp

    array=array[tmp_max_index:]
    array.reverse()        

    first=0

    
    for i in range(0,len(array)):    #가장큰것 기준 좌우 체크
        if array[i]>first:
            first=array[i]
        else:
            tmp=first-array[i]
            rain+=tmp

    print(rain)        

