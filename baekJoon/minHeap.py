import heapq

if __name__ == "__main__":
    n=int(input())
    arr=[int(input()) for _ in range(n)]

    hq=[]

    for a in arr:
        if a==0:
            
            if len(hq)==0:
                print('0')
            else:
                hpop=heapq.heappop(hq)
                print(hpop)

        else:
            heapq.heappush(hq,a)

