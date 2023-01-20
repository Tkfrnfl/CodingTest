#-*- coding:utf-8 -*-
import heapq

if __name__ == "__main__":
    tmp_input=list(map(int, input().split()))
    n=tmp_input[0]
    m=tmp_input[1]
    x=tmp_input[2]

    inf=int(1e5)

    go_graph=[[]for i in range(n+1)]
    back_graph=[[]for i in range(n+1)]

    for i in range(m):
        a,b,c=map(int, input().split())
        go_graph[b].append((a,c))
        back_graph[a].append((b,c))

    go_distance=[inf]*(n+1)
    back_distance=[inf]*(n+1)

  
    def dijkstra(start):
        q=[]
        heapq.heappush(q,(0,start))
        go_distance[start]=0

        while q:
            dist,now=heapq.heappop(q)

            if go_distance[now]<dist:
                continue
            for i in go_graph[now]:
                cost=dist+i[1]

                if cost<go_distance[i[0]]:
                    go_distance[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))
    def dijkstra2(start):
        q=[]
        heapq.heappush(q,(0,start))
        back_distance[start]=0

        while q:
            dist,now=heapq.heappop(q)

            if back_distance[now]<dist:
                continue
            for i in back_graph[now]:
                cost=dist+i[1]

                if cost<back_distance[i[0]]:
                    back_distance[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))                
    
    dijkstra(x)
    dijkstra2(x)

    tmp_max=0
    for i in range(1,n+1):
        tmp_max=max(tmp_max,go_distance[i]+back_distance[i])
    print(tmp_max)    
    # graph=[[inf]*(n+1)for _ in range(n+1) ]

    # for i in range(n):
    #         graph[i][i]=0

    # for idx,val in enumerate(array):
    #     graph[val[0]][val[1]]=val[2]

    # for k in range(1,n+1):      #플루이드 알고리즘
    #     for a in range(1,n+1):
    #         for b in range(1,n+1):
    #             graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

    # tmp_max=0

    # for i in range(1,n+1):      #가고 오는데 걸리는 시간
    #     if graph[i][x]!=inf and graph[x][i]!=inf:
    #         tmp_max=max(tmp_max,graph[i][x]+graph[x][i])
    
    # print(tmp_max)