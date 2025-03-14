import sys
import heapq

def dijkstra(max_cost):

    pq=[]
    heapq.heappush(pq,(0,1))

    dist =[float('inf')]*(n+1)
    dist[1]=0

    while pq:
        paid_cnt,node=heapq.heappop(pq)

        if node==n:
            return paid_cnt
        
        for next_node,cost in graph[node]:
            new_paid_cnt=paid_cnt+(cost>max_cost)
            if new_paid_cnt<dist[next_node]:
                dist[next_node]=new_paid_cnt
                heapq.heappush(pq,(new_paid_cnt,next_node))

    return float('inf')          


n, p, k = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(p):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))


left,right= 0,10**6
answer=-1

while left<=right:
    mid =(left+right)//2

    if dijkstra(mid)<=k:
        answer=mid
        right=mid-1
    else:
        left=mid+1

print(answer)