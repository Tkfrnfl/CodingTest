#-*- coding:utf-8 -*-
import math

if __name__=="__main__":
    #원형 리스트를 만들어 1,0 1,1  2,1 등의 조합 순으로 전체 탐색
    num=int(input())
    a,b = map(int, input().split())

    array_a=[]
    array_b=[]

    for _ in range(a):
        array_a.append(int(input()))
    for _ in range(b):
        array_b.append(int(input()))

    array_a.sort()
    array_b.sort()

    array_a.extend(array_a)        
    array_b.extend(array_b)

    ans=0

    size_a=[]
    size_b=[]

    for i in range(a+1):
        for m in range(a):
            if sum(array_a[m:m+i])==num:
                ans+=1
            if i!=0 and i!=a:
                size_a.append(sum(array_a[m:m+i]))    
        if i==a:
            size_a.append(sum(array_a[0:a]))

    for i in range(b+1):
        for m in range(b):
            if sum(array_b[m:m+i])==num:
                ans+=1
            if i!=0 and i!=b:
                size_b.append(sum(array_b[m:m+i]))      
        if i==b:
            size_b.append(sum(array_b[0:b]))
    # print(size_a)
    # print(size_b)
    size_a.sort()
    size_b.sort()


    for n in range(len(size_b)):
        start=0
        end=len(size_a)
        m=int((start+end)/2)

        while start<end:
            # print(start)
            # print(m)
            # print(end)
            # print("-----")
            if size_a[m]+size_b[n]<num:
                start=m+1
                m=int((start+end)/2)
            elif size_a[m]+size_b[n]>num:
                end=m-1
                m=int((start+end)/2)
            elif size_a[m]+size_b[n]==num:             
                break
        
        if m<len(size_a):
            m=size_a.index(size_a[m])
            while (size_a[m]+size_b[n])==num:
                ans+=1
                m+=1
                if m>=len(size_a):
                    break
       

    print(ans)  
