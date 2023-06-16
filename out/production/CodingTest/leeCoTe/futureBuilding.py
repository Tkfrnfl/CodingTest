#-*- coding:utf-8 -*-
def solution():
    n=5
    m=7
    num=[[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5]]
    x=4
    k=5

    visit=[0]*10
    dist=[1001]*10

    for i in range(0,len(num)):
        if num[i][0]==1:
            visit[num[i][1]]=1
            dist[num[i][1]]=1
        else:
            if visit[num[i][0]]==1:
                if visit[num[i][1]]==0:
                    dist[num[i][1]]=2
    print(dist)
if __name__ == "__main__":
	solution()      