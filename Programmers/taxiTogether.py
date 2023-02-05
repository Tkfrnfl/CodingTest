#-*- coding:utf-8 -*-
import heapq

inf=int(1e7)
graph=[]
distance=[inf]*200
answer = 0

def dijkstra(start):
    global distance
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


def solution(n, s, a, b, fares):
    global graph
    global answer
    global distance
    graph=[[]for i in range(int(n*n/2))]

    for i in range(len(fares)):
        graph[fares[i][0]].append((fares[i][1],fares[i][2]))
        graph[fares[i][1]].append((fares[i][0],fares[i][2]))

    dijkstra(s)  
    together_dist=distance  
    
    answer=inf
    #min_b=inf

    for i in range(n+1):
        if together_dist[i]!= inf:
            distance=[inf]*200
            #print(together_dist)
            dijkstra(i)
            answer=min(answer,together_dist[i]+distance[a]+distance[b])
            #min_b=min(min_b,together_dist[i]+distance[b])


    #print(answer)
    return answer


## 답은 맞다. 하지만 몇개 런타임에러
## >> 어차피 다익스트라 전체를 상대로 다시 돌리기에, 처음에 다익스트라 와셜로 돌릴것. 

if __name__ == "__main__":
    solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])