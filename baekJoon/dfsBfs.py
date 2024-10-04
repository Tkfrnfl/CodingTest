from collections import deque


if __name__ == "__main__":
    n,m,v = map(int, input().split())
    array=[list(map(int, input().split())) for _ in range(m)]

    graph =[[]for _ in range(n+1)]
    df=[]
    bf=[]

    def find():
        global array ,graph
        
        for i in array:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

    def dfs(visited,s):
        global df,graph

        df.append(s)
        visited[s] =True
        for i in sorted(graph[s]):
            if not visited[i]:
                dfs(visited,i)

    def bfs (v) :
        global bf,graph,n
        visited=[False] *(n+1)

        queue =deque([v])
        visited[v] =True

        while queue:
            now =queue.popleft()
            
            bf.append(now)
            for i in sorted(graph[now]):
                if not visited[i]:
                    queue.append(i)
                    visited[i] =True


    find()    

    visited=[False] * (n+1)
    
    dfs(visited,v)
    bfs(v)

    print(" ".join(map(str, df)))
    print(" ".join(map(str, bf)))