# -*- coding:utf-8 -*-
if __name__ == "__main__":
    n=int(input())
    array=list(map(int,input().split()))

    tmp_list=[]
    count=0
    tmp_list.append(array[0])
    for i in range (1,n):
        
        for j in range(len(tmp_list)):
            tmp_list[j]+=array[i]
            if tmp_list[j]==0:
                count+=1
        tmp_list.append(array[i])


    print(count)    