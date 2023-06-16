#-*- coding:utf-8 -*-
from collections import deque

if __name__ == "__main__":
    n=int(input())
    array=[list(map(int, input().split())) for _ in range(n)]
    
    baby_shark='eat'
    baby_shark_loc=(0,0)
    baby_shark_size=2
    baby_shark_stack=0
    for i in range(0,n):        #첫 상어 위치
        for j in range(0,n):
            if array[i][j]==9:
                baby_shark_loc=(i,j)

    def stack_check():
            baby_shark_stack=baby_shark_stack+1
            if baby_shark_stack==baby_shark_size:
                baby_shark_stack=0
                baby_shark_size=baby_shark_size+1

    dy=[-1,1,0,0] #상하
    dx=[0,0,-1,1] #좌우
    tmp=[]

    def bfs(x,y,size):
        distance = [[0] * n for _ in range(n)]
        visited = [[0] * n for _ in range(n)]

        q=deque()
        q.append((x,y))
        visited[x][y]=1
        tmp=[]
        while q:
            cur_x,cur_y=q.popleft()

            for i in range(4):
                nx=cur_x+dx[i]
                ny=cur_y+dy[i]

                if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
                    if array[nx][ny] <= baby_shark_size:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[cur_x][cur_y] + 1
                        if array[nx][ny] < baby_shark_size and array[nx][ny] != 0:
                            tmp.append((nx,ny,distance[nx][ny]))
        return sorted(tmp,key=lambda x: (-x[2],-x[0],-x[1]))      



    result = 0
    while 1:
        shark = bfs(baby_shark_loc[0],baby_shark_loc[1],2)

        if len(shark) == 0:
            break
        
        nx,ny,dist =shark.pop()
        result += dist
        array[baby_shark_loc[0]][baby_shark_loc[1]],array[nx][ny] = 0,0
        baby_shark_loc=(nx,ny)
        baby_shark_stack += 1
        if baby_shark_stack == baby_shark_size:
            baby_shark_size += 1
            baby_shark_stack = 0
    print(result)       
    # def next_loc(now_i,now_j):
    #     if now_j>0:   #좌
    #         if array[now_i][now_j-1]<baby_shark_size:
    #             stack_check()
    #             baby_shark_loc=(now_i,now_j-1)
    #             return

    #     elif now_i-1>0:   #상
    #         if array[now_i-1][now_j]<baby_shark_size:
    #             stack_check()
    #             baby_shark_loc=(now_i-1,now_j)
    #             return

    #     elif now_j+1<n:   #우
    #         if array[now_i][now_j+1]<baby_shark_size:
    #             stack_check()
    #             baby_shark_loc=(now_i,now_j+1)
    #             return

    #     elif now_i+1<n:   #하
    #         if array[now_i+1][now_j]<baby_shark_size:
    #             stack_check()
    #             baby_shark_loc=(now_i+1,now_j)
    #             return
    #     else: next_loc(now_i,now_j-1)
        