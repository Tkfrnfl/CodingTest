#-*- coding:utf-8 -*-

if __name__ == "__main__":
    n=int(input())
    m=int(input())
    array=[list(map(int,input().split()))for _ in range(n)]
    order=list(map(int,input().split()))
    
    answer='YES'
    for i in range(len(order)):
        tmp=0
        for j in range(len(array[order[i]-1])):

            if array[order[i]-1][j]==1:
                tmp+=1
            elif j==n-1:
                if tmp==0:
                    answer='NO'

    print(answer)            

