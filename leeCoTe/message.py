#-*- coding:utf-8 -*-
def solution():
    n=3
    m=2
    c=1
    visit=[0]*10
    way=[[1,2,4],[1,3,2]]
    distance=[10001]*10

    visit[1]=1
    for i in range(1,n+1):
        if visit[i]!=1:
            visit[i]=1  #방문처리

            for j in range(0,len(way)):
                if way[j][1]==i:   #보려는 연결노드의 거리값정보이면
                    cost=way[j][2] #거리값정보를 가져와서
                    if cost< distance[i]:
                        distance[i]=cost    #원래 거리보다 짧을시 저장
    print(distance)
if __name__ == "__main__":
	solution()  