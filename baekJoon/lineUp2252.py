# -*- coding:utf-8 -*-

from collections import deque
# 위상정렬 문제

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(m)]
    # 

    graph_in=[0] * (n+1)
    graph_out= [[]for _ in range(n+1)]

    # in 방향 가중치 저장 ,out 방향 목표점 저장
    for arr in array:
        graph_in[arr[1]]+=1
        graph_out[arr[0]].append(arr[1])

    ans=[]
    q =deque()


    for i in range(1,n+1):
        if graph_in[i]==0:
            q.append(i)
            ans.append(i)

    while q:
        num=q.popleft()
        for gout in graph_out[num]:
            graph_in[gout]-=1
            if graph_in[gout]==0:
                q.append(gout)
                ans.append(gout)

    for i in ans:
        print(i, end=" ")                
    