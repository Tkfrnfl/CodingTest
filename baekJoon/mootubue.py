#-*- coding:utf-8 -*-
import heapq

if __name__=="__main__":
    n,q=map(int,input().split())
    inf=int(1e9)
    #array=[inf for j in range(n+1) for i in range(n+1)]
    array=[[]for i in range(n+1)]
    q=[]
    dist =[inf for j in range(n+1) for i in range(n+1)]

    for i in range(n-1):
        pi,qi,ri=map(int,input().split())

        #array[pi][qi]=ri
        #array[pi].append((qi,ri))
        heapq.heappush(q,(pi,qi,ri))
        dist[pi][qi]=ri

    question=[]

    for i in range(q):
       ki,vi=map(int,input().split())
       question.append((ki,vi)) 

    

    i=0
    while q:

        pi,qi,ri=heapq.heappop(q)
        
        dist[pi][qi]=ri
        dist[qi][pi]=ri


