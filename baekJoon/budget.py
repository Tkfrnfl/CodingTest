#-*- coding:utf-8 -*-

if __name__ == "__main__":
    n=int(input())
    array=list(map(int,input().split()))
    m=int(input())

    l=0
    r=1000000000
    
    ans_max=0
    ans=0
    while l<r-1:
        mid=int((l+r)/2)

        tmp=0
        for i in range(n):
            if array[i]<=mid:
                tmp+=array[i]
            else:
                tmp+=mid
        if tmp>m:
            r=mid
        else:
            l=mid
            if tmp>ans_max:
                ans_max=tmp 
                ans=mid
    if ans>max(array):
        ans=max(array)            
    print(ans)        