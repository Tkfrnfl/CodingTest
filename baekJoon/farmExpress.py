# -*- coding:utf-8 -*-
import heapq

if __name__ == "__main__":
    n,m = map(int,input().split())
    array = [list(map(int, input().split())) for _ in range(m)]

    INF= int(1e9)
    graph=[[]for _ in range(n+1)]
    answer = INF

    def find():
        global graph

        for i in array:   
            graph[i[0]].append((i[1],i[2]))
            graph[i[1]].append((i[0],i[2]))

    def start(st):
        distance =[INF]*(n+1)
        hq=[]
        distance[st]=0
        heapq.heappush(hq,(0,st))

        while hq:
            #print(distance)
            cost,now=heapq.heappop(hq)

            if cost > distance[now]:
                continue
            for i in graph[now]:
                if distance[i[0]] > i[1]+cost:
                    distance[i[0]] = i[1]+cost
                    heapq.heappush(hq,(i[1]+cost,i[0]))

        return distance
    
    find()
    dist=start(1)
    print(dist[n])