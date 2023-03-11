if __name__ == "__main__":
    n,l = map(int, input().split())
    array=[list(map(int, input().split())) for _ in range(n)]


    ans=0
    now_stack=1
    before_num=0
    for i in range(n):
        # print(i)
        
        # print('d'+str(ans)+'d')
        for j in range(n):
            if i>=n:
                break
            if j==0:
                before_num=array[i][j]
                continue
            
            if array[i][j]-before_num==0: #같은경우
                now_stack+=1
            elif array[i][j]-before_num==1: # 한칸 더큰 경사
                if now_stack<l:             # 스택 미만이면 다음줄로
                    now_stack=1
                    i+=1
                    j=-1
                    continue
                else:
                    before_num=array[i][j]    
            elif array[i][j]-before_num==-1: # 한칸 더작은 경사
                slope_check=True
                if j+l-1 >=n:                    #l보다 남은게 적으면 다음줄로
                    now_stack=1       
                    i+=1
                    j=-1      
                    continue                        
                for k in range(1,l):
                    if array[i][j+k]!=array[i][j]:
                        slope_check=False
                if slope_check==False:
                    now_stack=1         # 다음줄로
                    i+=1
                    j=-1 
                    continue
                else:
                    now_stack=1
                    j+=(l-1) 
                    before_num=0
            else:                #2칸이상 차이 다음줄로
                now_stack=1         
                i+=1
                j=-1 
                continue
            if j==n-1:
                ans+=1
                now_stack=1 
                before_num=0      

    now_stack=1
    before_num=0                             
    for j in range(n):
        print(j)
        
        print('*'+str(ans)+'*')
        for i in range(n):  
            print(i,j)
            if j>=n:
                break     
            if i==0:
                before_num=array[i][j]
                continue
            if array[i][j]-before_num==0: #같은경우
                now_stack+=1
            elif array[i][j]-before_num==1: # 한칸 더큰 경사
                if now_stack<l:             # 스택 미만이면 다음줄로
                    now_stack=1
                    j+=1
                    i=-1
                    continue
                else:
                    before_num=array[i][j]    
            elif array[i][j]-before_num==-1: # 한칸 더작은 경사
                slope_check=True
                if i+l-1 >=n:                    #l보다 남은게 적으면 다음줄로
                    now_stack=1       
                    j+=1
                    i=-1      
                    continue                        
                for k in range(1,l):
                    if array[i+k][j]!=array[i][j]:
                        slope_check=False
                if slope_check==False:
                    now_stack=1         # 다음줄로
                    j+=1
                    i=-1 
                    continue
                else:
                    print('??')
                    now_stack=1
                    i+=(l-1) 
                    before_num=0
                    print(i,j)
            else:                #2칸이상 차이 다음줄로
                now_stack=1         
                j+=1
                i=-1 
                continue        
            if i==n-1:
                ans+=1
                now_stack=1 
                before_num=0   
            
    print(ans)            