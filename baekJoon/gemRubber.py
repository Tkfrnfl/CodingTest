import heapq

if __name__ == "__main__":
    n,k = map(int, input().split())
    gem=[list(map(int, input().split())) for _ in range(n)]
    bag=[int(input()) for _ in range(k)]
    bag.sort()
    gem.sort()

    hq =[]
    ans=0
    cnt=k
    g_cnt=0
    for j in range(len(bag)):
        
        while cnt>0 and g_cnt<n and gem[g_cnt][0]<=bag[j]:
            heapq.heappush(hq,-gem[g_cnt][1])
            g_cnt+=1

        if hq:
            #print(hq)
            ans-=heapq.heappop(hq)
            cnt-=1


    print(ans)            

