#-*- coding:utf-8 -*-
from collections import deque

if __name__ == "__main__":
    n=int(input())
    m=int(input())
    array=[list(map(int,input().split()))for _ in range(n)]
    order=list(map(int,input().split()))
    
    answer='YES'

    for i in range(1,m):
        if array[order[i-1]-1][order[i]-1]==1:
            continue
        else:
            q= deque()

            q.append(order[i-1])

            visited=[False]*(n + 1)
            reach=False

            while q:
                p = q.popleft()

                if visited[p]:
                    continue
                else:
                    visited[p]=True

                if p==order[i]:
                    reach=True
                    break

                for j in range(n):
                    if array[p-1][j]==1 and not visited[j+1]:
                        q.append(j+1)    

            if reach:
                continue
            else:
                answer='NO'
                break            


 


    print(answer)            

