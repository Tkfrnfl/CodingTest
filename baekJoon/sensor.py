# -*- coding:utf-8 -*-

if __name__ == "__main__":
    n= int(input())
    k= int(input())

    array = list(map(int, input().split())) 

    array.sort()

    blank_list=[]

    for i in range(1,n): # 센서간 거리 저장
       blk=array[i]-array[i-1]

       blank_list.append((blk,i-1))

    blank_list.sort(reverse=True)

    cut_idx=[]

    for i in range(k-1):    # 구간 나눌 idx 저장
        if i>n-2:
            break
        cut_idx.append(blank_list[i][1])

    ans=0
    start=array[0]
    for i in range(n):
        if i in cut_idx:
            ans+=array[i]-start
            if i+1<n:
                start=array[i+1]

    ans+= array[n-1]-start

    print(ans)

    