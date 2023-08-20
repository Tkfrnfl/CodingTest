def solution(game_board, table):
    
    n=len(game_board[0])
    
    visited=[[0 for _ in range(n)]for _ in range(n)]
    visited_table=[[0 for _ in range(n)]for _ in range(n)]
    
    table_shape=[]
    board_shape=[]
    
    board_stack=[] 
    table_stack=[]
    
    yy=[1,-1,0,0]
    xx=[0,0,1,-1]
    
    def dfs(a,b):
        global board_stack
        board_stack.append([a,b])
        visited[a][b]=1
        
        for i in range(4):
            y=y+yy[i]
            x=x+xx[i]    
            
            if 0<=y<n and 0<=x<n and visited[y][x]==0 and game_board[y][x]==0:
                visited[y][x]=1
                board_stack.append((y,x))
                dfs(y,x)
        return        
     
    def dfs_table(a,b):                 #for table dfs
        global table_stack
        table_stack.append([a,b])
        visited_table[a][b]=1
        
        for i in range(4):
            y=y+yy[i]
            x=x+xx[i]    
            
            if 0<=y<n and 0<=x<n and visited_table[y][x]==0and table[y][x]==1:
                visited_table[y][x]=1
                table_stack.append((y,x))
                dfs_table(y,x)
        return        
        
    def correction(tmp_list):
            x=100
            y=100
            
            for i in range(len(tmp_list)):
                y=min(y,tmp_list[i][0])
                x=min(x,tmp_list[i][1])
            return y,x    
    
    def rotate_2d(tmp_list):
        array=[]

        for i in range(len(tmp_list)):
            y=tmp_list[i][1]
            x=n-1-tmp_list[i][0]
            array.append([y,x])
        return array    
        
            
        
    for i in range(n):              #game board check
        for j in range(n):
            if game_board[i][j]==0:
                dfs(i,j)
                board_shape.append(board_stack)
                board_stack=[]
                
                
    for i in range(n):              #table check
        for j in range(n):
            if table[i][j]==1:
                dfs_table(i,j)
                table_shape.append(table_stack) 
                table_stack=[]
     
    #max puzzle search
    for i in range(len(board_shape)):
        y,x=correction(board_shape[i])
        for k in range(len(board_shape[i])):
                board_shape[i][k][0]-=y
                board_shape[i][k][1]-=x
                
        for j in range(len(table_shape)):  
            tmp0=[]
            tmp1=[]
            tmp2=[]
            tmp3=[]
            for r in range(4):
                if r==0:
                    tmp0=table_shape[j]
                    y,x=correction(tmp0)
                    for k in range(len(tmp0)):
                        board_shape[i][k][0]-=y
                        board_shape[i][k][1]-=x
                elif r==1:
                    tmp1=rotate_2d(table_shape[j])
                    y,x=correction(tmp1)
                    for k in range(len(tmp1)):
                        board_shape[i][k][0]-=y
                        board_shape[i][k][1]-=x
                elif r==2:
                    tmp2=rotate_2d(tmp1)
                elif r==3:
                    tmp3=rotate_2d(tmp2)
                    
                        
                        
                           
                
                        
    answer = -1
    return answer