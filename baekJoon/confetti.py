import copy

if __name__ == "__main__":
    arr = [list(map(int, input().split())) for _ in range(10)]


    confetti_12345=[0]*6

    visited =[[False]*10 for _ in range(10)]

    ans=0

    def consist1(x,y):
        global arr,visited

        visit_copy =copy.deepcopy(visited)
        width =1

        for i in range(1,10-x):

            if x+i <10 and y+i<10:
                for j in range(1,i+1):
                    visit_copy[x][y+j]=True
                    if arr[x][y+j]==0:
                        return width

                for k in range(1,i+1):
                    visit_copy[x+k][y]=True
                    if arr[x+k][y] ==0:
                        return width    
                if width>=5:
                    return 5

                if arr[x+i][y+i] ==0:
                    return width
                visit_copy[x+i][y+i]=True  

                
                visited= visit_copy  
                width+=1
        
        return width            



    for i in range(10):
        brk = False
        for j in range(10):
            if arr[i][j]==1 and not visited[i][j]:
                mx_len=consist1(i,j)
                # print(i,j)
                # print(mx_len)

                if confetti_12345[mx_len]<5:
                    confetti_12345[mx_len]+=1
                    ans+=1
                else:
                    ans=-1
                    brk =True
                    break
        if brk:
            break            

    print(ans)                
