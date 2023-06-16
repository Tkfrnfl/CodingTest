import heapq
import math

if __name__ == "__main__":
    n,l,r = map(int, input().split())
    array=[list(map(int, input().split())) for _ in range(n)]
    
    moved=0

    def find():
        global moved
        checked=[[0 for i in range(n)]for k in range(n)]
        up_down=[0,0,1,-1]
        right_left=[1,-1,0,0]
        movecheck=False
        print(array)
        for i in range(n):
            for k in range(n):            
                q=[]
                heapq.heappush(q,(i,k))

                if checked[i][k]==1:
                    continue

                checked[i][k]=1

                for j in range(4):
                    x=i+up_down[j]
                    y=k+right_left[j]

                    if 0<=x<n and 0<=y<n:

                        for idx,now in enumerate(q):
                            for j in range(4):
                                if l<=abs(array[now[0]][now[1]]-array[x][y])<=r:
                                    checked[x][y]=1
                                    heapq.heappush(q,(x,y))

                        if len(q)>1:
                            movecheck=True
                            tmp=0
                            for idx,val in enumerate(q):
                                tmp+=array[val[0]][val[1]]
                            for idx,val in enumerate(q):
                                array[val[0]][val[1]]=math.floor(tmp/len(q))    

        if movecheck:
            moved+=1
            find()

    find()     
    print(moved)   
