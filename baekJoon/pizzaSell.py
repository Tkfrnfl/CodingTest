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

    array_a.extend(array_a)        
    array_b.extend(array_b)

    ans=0

    
    for i in range(0,2)

    for i in range(2,a):
        for j in range(2,b):
            tmp_a=0
            tmp_b=0
            for m in range(len(array_a)):
                sum_a=0
                tmp_a=array_a[m:m+i]
                
                
                if sum(tmp_a)==num:
                    ans+=1
                    continue
                if sum(tmp_a)>num:
                    continue
                for n in range(len(array_b)):
                    tmp_b=array_b[n:n+j]
     
                    if sum(tmp_a)+sum(tmp_b)==num:
                        #print(i,m,j,n)
                        print(tmp_a)
                        print(tmp_b)
                        ans+=1

    print(ans)                    