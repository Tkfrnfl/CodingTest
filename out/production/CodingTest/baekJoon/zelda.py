import heapq

if __name__ == "__main__":
    inf=int(1e4)
    def dijkstra(distance,arra,n):
        q=[]
        heapq.heappush(q,(array[0][0],(0,0)))
        distance[0][0]=array[0][0]

        up_down=[0,0,1,-1]
        right_left=[1,-1,0,0]

        while q:
            dist,now=heapq.heappop(q)

            # if distance[now[0]][now[1]]<dist:     # 접근한곳 재접근을 위해 해당 코드 주석
            #     continue
            for i in range(4):

                x=now[0]+right_left[i]
                y=now[1]+up_down[i]
                if 0<=y<n and 0<=x<n:
                    cost= dist+array[x][y]

                    if cost<distance[x][y]:
                        distance[x][y]=cost
                        heapq.heappush(q,(cost,(x,y)))
        #print(distance)
        return distance[-1][-1]

    ans=[]

    while True:
        n=int(input())
        if n==0:
            break
        else:
            array=[list(map(int, input().split())) for _ in range(n)]
            distance=[[inf for col in range(n)] for row in range(n)]
            tmp=dijkstra(distance,array,n)
            ans.append(tmp)

    for i in range(len(ans)):
        print('Problem '+str(i+1)+': '+str(ans[i]))        