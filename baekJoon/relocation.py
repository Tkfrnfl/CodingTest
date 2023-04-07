#-*- coding:utf-8 -*-
import heapq
from itertools import permutations 

if __name__ == "__main__":
    n,m,k=map(int,input().split())
    array_market=[]
    Inf=int(1e9)

    for i in range(k):
        array_market.append(int(input()))

    graph=[[Inf]*(n+1)for _ in range(n+1)]

    for a in range(1,n+1):
        for b in range(1,n+1):
            if a==b:
                graph[a][b]==0

    for _ in range(m):
        a,b,c=map(int,input().split())       
        graph[a][b]=c
        graph[b][a]=c

    for i in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])  
                graph[b][a]=min(graph[a][b],graph[a][i]+graph[i][b])  

    # graph=[[]for i in range(n)]
    # distance=[Inf]*(n+1)

    # for num in range(m):
    #     i,j,l=map(int,input().split())  
    #     graph[i].append((j,l))
    #     graph[j].append((i,l))

    # def dijk(start):
    #     q=[]
    #     heapq.heappush(q,(0,start))
    #     distance[start]=0

    #     while q:
    #         dist,now=heapq.heappop(q)
    #         if distance[now]<dist:
    #             continue
            
    #         for i in graph[now]:
    #             cost=dist+i[1]
    #             if cost<distance[i[0]]:
    #                 distance[i[0]]=cost
    #                 heapq.heappush(q,(cost,i[0]))

    tmp_per=[]

    def permutation(arr, r):
        # 1.
        arr = sorted(arr)
        used = [0 for _ in range(len(arr))]

        def generate(chosen, used):
            # 2.
            if len(chosen) == r:
                tmp_per.append(tuple(chosen))
                return
        
        # 3.
            for i in range(len(arr)):
                if not used[i]:
                    chosen.append(arr[i])
                    used[i] = 1
                    generate(chosen, used)
                    used[i] = 0
                    chosen.pop()
        generate([], used)



    #tmp_per=list(permutations(array_market,2))
    permutation(array_market,3)
    tmp_min=Inf

    for num_j in range(1,n+1):
        if num_j not in array_market:      
            for num_i in range(len(tmp_per)):
                tmp_sum=0
                tmp_sum+=graph[num_j][tmp_per[num_i][0]]
                for num_k in range(k-1):
                    tmp_sum+=graph[tmp_per[num_i][num_k]][tmp_per[num_i][num_k+1]]
                tmp_sum+=graph[tmp_per[num_i][k-1]][num_j]

                tmp_min=min(tmp_min,tmp_sum)      
    print(tmp_min)        
                
