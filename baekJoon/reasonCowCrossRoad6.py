# -*- coding:utf-8 -*-
from collections import deque

if __name__ == "__main__":
    n, k,r = map(int, input().split())
    arr_r = [list(map(int, input().split())) for _ in range(r)]
    arr_k = [list(map(int, input().split())) for _ in range(k)]

    ans =0

    graph={}


    # 각 길마다 갈수있는곳 저장
    for ar in arr_r:
        if (ar[0],ar[1]) not in graph:
            graph[(ar[0],ar[1])]=[]
        graph[(ar[0],ar[1])].append((ar[2],ar[3]))

        if (ar[2],ar[3]) not in graph:
            graph[(ar[2],ar[3])]=[]
        graph[(ar[2],ar[3])].append((ar[0],ar[1]))        


    # print(graph)
    def bfs(s,e,v):
        global graph


        q= deque()

        q.append(tuple(s))

        while q:
            print(q)
            p_list= q.popleft()
            v[p_list[0]][p_list[1]]= True

            if p_list == e:
                return True

            
            if p_list not in graph:
                print(p_list, e)
                return False

            for lis in graph[p_list]:
                #print(graph[p_list])
                if not v[lis[0]][lis[1]]:
                    q.append(lis)


    visited=[[False]*(n+1) for _ in range(n+1)]

    for i in range(k):
        for j in range(i+1,k):
            if not bfs(arr_k[i],arr_k[j],visited):
                ans+=1

    print(ans)            